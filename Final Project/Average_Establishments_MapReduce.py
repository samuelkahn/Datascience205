# -*- coding: utf-8 -*-
"""
@author: samuelkahn
"""

from mrjob.job import MRJob

 
class AverageEstablishmentsFIPSCode(MRJob):

    def mapper(self, line_no, line):
        ### process line by line
        cells = line.split(',')        
        fips=cells[0]

        try:
            estabs=cells[-8]
        ### Yield fips as key, average quarterly establishment count for year as value
            yield fips,float(estabs)
        except (ValueError,IndexError):
            yield 0,0.0

    def reducer(self, fips_code, estabs_gen):
        fips_code=str(fips_code)
        count=0
        num=0
        ### Sum up values and divide by number of values to get average
        while True:
            try:
                count+=estabs_gen.next()
                num+=1
            except StopIteration:
                break
        ### Yield fips and average
        yield fips_code[1:-1],int(count/num)

        
if __name__ == '__main__':
    AverageEstablishmentsFIPSCode.run()