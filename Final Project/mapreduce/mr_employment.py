# -*- coding: utf-8 -*-
"""
Created on Thu Dec 18 2014
@author: samuelkahn mhayes
"""
from mrjob.job import MRJob

 
class YearlyEmploymentLevels(MRJob):

    def mapper(self, line_no, line):
        cells = line.split(',')        
        ### sum up the employee level for each month in the quarter
        try:
            agglvl = cells[3]
            if agglvl=="73":
                fips=str(cells[0])[1:-1]
                empl_lvl=sum([float(cells[-5]),float(cells[-6]),float(cells[-7])])/3
                yield fips,float(empl_lvl)
        except (ValueError,TypeError,IndexError):
            yield 0,0.0

    def reducer(self, fips_code, empl_lvl_gen):
        fips_code=str(fips_code)
        count=0
        ### Sum up values and divide by 4
        while True:
            try:
                count+=empl_lvl_gen.next()
            except StopIteration:
                break
        ### Yield fips and average employee level
        yield fips_code,int(count/4)

        
if __name__ == '__main__':
    YearlyEmploymentLevels.run()
