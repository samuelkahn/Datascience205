# -*- coding: utf-8 -*-
"""
Created on Thu Dec 18 2014
@author: samuelkahn mhayes
"""

from mrjob.job import MRJob

 
class TotalWagesFIPSCode(MRJob):

    def mapper(self, line_no, line):
        cells = line.split(',')        
        ### sum up the total wages
        try:
            agglvl = cells[3]
            if agglvl=="73":
                fips=str(cells[0])[1:-1]
                wages=cells[-4]
                yield fips,float(wages)
        except (ValueError,TypeError,IndexError):
            yield 0,0.0

    def reducer(self, fips_code, wages_gen):
        fips_code=str(fips_code)
        count=0
        ### Sum up values
        while True:
            try:
                count+=wages_gen.next()
            except StopIteration:
                break
        ### Yield fips and total wages
        yield fips_code,count

        
if __name__ == '__main__':
    TotalWagesFIPSCode.run()
