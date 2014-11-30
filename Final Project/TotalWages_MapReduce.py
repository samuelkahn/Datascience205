# -*- coding: utf-8 -*-
"""
@author: samuelkahn
"""

from mrjob.job import MRJob

 
class TotalWagesFIPSCode(MRJob):

    def mapper(self, line_no, line):
        cells = line.split(',')        
        fips=cells[0]

        try:
            wages=cells[-4]
            yield fips,float(wages)
        except (ValueError,IndexError,ValueError):
            yield 0,0.0

    def reducer(self, fips_code, wages_gen):
        fips_code=str(fips_code)
        count=0
        while True:
            try:
                count+=wages_gen.next()
            except StopIteration:
                break
        yield fips_code[1:-1],count

        
if __name__ == '__main__':
    TotalWagesFIPSCode.run()