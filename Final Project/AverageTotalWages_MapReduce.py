# -*- coding: utf-8 -*-
"""
@author: samuelkahn
"""

from mrjob.job import MRJob

 
class TotalWagesFIPSCode(MRJob):

    def mapper(self, line_no, line):
        cells = line.split(',')        
        fips=cells[0]
        wages=cells[-4]
       ## yield fips code, and total wage by quarter
        try:
            yield fips,float(wages)
        except ValueError:
            yield 0,0.0

    def reducer(self, fips_code, wages_gen):
        fips_code=str(fips_code)
        count=0
        ### Sum the values to get the total
        while True:
            try:
                count+=wages_gen.next()
            except StopIteration:
                break
        ### Yield fips code and aggregates 
        yield fips_code[1:-1],count

        
if __name__ == '__main__':
    TotalWagesFIPSCode.run()