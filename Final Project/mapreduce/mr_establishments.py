# -*- coding: utf-8 -*-
"""
Created on Thu Dec 18 2014
@author: samuelkahn mhayes
"""

from mrjob.job import MRJob

 
class AverageEstablishmentsFIPSCode(MRJob):

    def mapper(self, line_no, line):
        ### process line by line
        cells = line.split(',')        
        ### sum up the establishment counts
        try:
            agglvl = cells[3]
            if agglvl=="73":
                fips=str(cells[0])[1:-1]
                estabs=cells[-8]
                yield fips,float(estabs)
        except (ValueError,TypeError,IndexError):
            yield 0,0.0

    def reducer(self, fips_code, estabs_gen):
        fips_code=str(fips_code)
        count=0
        ### Sum up values and divide by 4
        while True:
            try:
                count+=estabs_gen.next()
            except StopIteration:
                break
        ### Yield fips and average establishments
        yield fips_code,int(count/4)

        
if __name__ == '__main__':
    AverageEstablishmentsFIPSCode.run()
