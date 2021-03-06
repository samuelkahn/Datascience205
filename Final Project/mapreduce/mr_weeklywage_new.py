# -*- coding: utf-8 -*-
"""
Created on Thu Dec 18 2014
@author: samuelkahn mhayes

NOT USED IN OUR PROJECT - concept for further exploration
"""

from mrjob.job import MRJob

 
class AverageIncomeFIPSCode(MRJob):

    def mapper(self, line_no, line):
        cells = line.split(',')
        ###print cells
        try:
            fips=str(cells[0])[1:-1]
            sector =int(cells[1])
            industry =int(cells[2])
            agglvl = cells[3]
            datkey = [fips,sector,industry]
            if agglvl == "73":
            ### Yield fips as key, average quarterly weekly wage
                weeklywages=float(cells[-4])/13
                empl_lvl=sum([float(cells[-5]),float(cells[-6]),float(cells[-7])])/3
                wagetuple=[float(weeklywages),float(empl_lvl)]
                yield datkey,wagetuple
        except (ValueError,TypeError,IndexError):
            yield [0,0,0],[0.0,0.0]

    """
    def reducer(self, fips_sector_industry, wagetuple):
        ### Sumarizes the user counts by adding them together.
        fips_code=fips_sector_industry[0]
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
    """

    def reducer(self, fips_sector_industry, wagetuple):
        """Sumarizes the user counts by adding them together. """
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
        yield fips_sector_industry,weeklywage

        
if __name__ == '__main__':
    AverageIncomeFIPSCode.run()
