# -*- coding: utf-8 -*-
"""
Created on Thu Dec 18 2014
@author: samuelkahn mhayes
"""

from mrjob.job import MRJob

 
class AverageIncomeFIPSCode(MRJob):

    def mapper(self, line_no, line):
        cells = line.split(',')        
        ### Yield fips as key, average quarterly weekly wage
        try:
            agglvl = cells[3]
            if agglvl=="73":
                fips=str(cells[0])[1:-1]
                weeklywages=float(cells[-4])/13
                empl_lvl=sum([float(cells[-5]),float(cells[-6]),float(cells[-7])])/3
                wagetuple=[float(weeklywages),float(empl_lvl)]
                yield fips,wagetuple
        except (ValueError,TypeError,IndexError):
            yield 0,[0.0,0.0]

    def reducer(self, fips_code, wagetuple):
        """Sumarizes the user counts by adding them together. """
        fips_code=str(fips_code)
        wagesum=0
        emplsum=0
        ### Sum quarterly weekly wages and divide by 4
        while True:
            try:
                x=wagetuple.next()
                wagesum+=x[0]
                emplsum+=x[1]
                weeklywage = wagesum/emplsum if emplsum>0 else 0
            except StopIteration:
                break
        ### Yield fips code and average income
        yield fips_code,weeklywage

        
if __name__ == '__main__':
    AverageIncomeFIPSCode.run()
