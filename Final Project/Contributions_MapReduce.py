# -*- coding: utf-8 -*-
"""
@author: samuelkahn
"""
### Data to sparse for early years, not actually ucsed
from mrjob.job import MRJob

class ContributionsFIPSCode(MRJob):

    def mapper(self, line_no, line):
        ### Take in line by line
        cells = line.split(',')        
        fips=cells[0]

        try:
            ### Yield contributions as value, fips as key
            contributions=cells[-2]
            yield fips,int(contributions)
        except (ValueError,IndexError):
            yield 0,0.0

    def reducer(self, fips_code, wages_gen):
        fips_code=str(fips_code)
        count=0
        ### Until we hit exception, sum values in generator to get total contributions
        while True:
            try:
                count+=wages_gen.next()
            except StopIteration:
                break
        ### Yield fips code, and sum of contributions
        yield fips_code[1:-1],count
        
if __name__ == '__main__':
    ContributionsFIPSCode.run()