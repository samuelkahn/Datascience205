# -*- coding: utf-8 -*-
"""
Created on Sun Nov 23 10:43:27 2014

@author: samuelkahn
"""
from mrjob.job import MRJob

 
class YearlyEmploymentLevels(MRJob):

    def mapper(self, line_no, line):
        cells = line.split(',')        
        fips=cells[0] 
        try:
            empl_lvl=sum([float(cells[-5]),float(cells[-6]),float(cells[-7])])/3
            yield fips,float(empl_lvl)
        except (ValueError,TypeError,IndexError):
            yield 0,0.0

    def reducer(self, fips_code, empl_lvl_gen):
        fips_code=str(fips_code)
        count=0
        num=0
        while True:
            try:
                count+=empl_lvl_gen.next()
                num+=1
            except StopIteration:
                break
        yield fips_code[1:-1],int(count/num)

        
if __name__ == '__main__':
    YearlyEmploymentLevels.run()