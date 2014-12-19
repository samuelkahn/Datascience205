# -*- coding: utf-8 -*-
"""
@author: samuelkahn
"""

from mrjob.job import MRJob

 
class AverageIncomeFIPSCode(MRJob):

    def mapper(self, line_no, line):
        cells = line.split(',')        
        fips=cells[0]
        wage=cells[len(cells)-1]
        ### Yield fips as key, average quarterly weekly wage
        try:
            yield fips,float(wage)
        except ValueError:
            yield 0,0.0

    def reducer(self, fips_code, wages_gen):
        """Sumarizes the user counts by adding them together. """
        fips_code=str(fips_code)
        count=0
        num=0
        ### Sum  quarterly weekly wages and divide to get average quarterly wages
        while True:
            try:
                count+=wages_gen.next()
                num+=1
            except StopIteration:
                break
        ### Yield fips code and average
        yield fips_code[1:-1],count/num

        
if __name__ == '__main__':
    AverageIncomeFIPSCode.run()
