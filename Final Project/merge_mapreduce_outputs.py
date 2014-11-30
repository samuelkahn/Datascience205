# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 11:24:41 2014

@author: samuelkahn
"""
import os
import csv

def main():
    ### Folders and Filenames
    folders=[str(x) for x in range(1990,2015)]
    path='/Users/samuelkahn/Desktop/Berkeley/DS205/Final Project'
    filenames=['_output.txt','_total_wages.txt','_estabs_count.txt','_employment_level.txt']
    ## Dictionary key:fips code, value:list wither each MR output
    data_dict = {}
    ### Loop over each folder
    for folder in folders:
        os.chdir(path+'/'+folder)
        ### Loop over each file in folder
        for index in range(0,len(filenames)):
            with open(folder+filenames[index]) as inputfile:
                ### For each line in file
                for line in inputfile:
                    (key, val) = line.split()
                    ### key is fips_code, value is list 
                    if index==0:
                        data_dict[key] = [val]
                    else:
                        data_dict[key].append(val)
        inputfile.close()
        ### Now open CSV for writing
        with open(folder+'_mapreduce_aggregate.csv', 'wb') as outputfile:
            writer = csv.writer(outputfile, delimiter=',')
            ### Write Header
            writer.writerow(['FIPS_CODE','Weekly_Wage','Total_Wages','Establishment_Count'\
            ,'Employment_Level'])
            ### Loop over all dictionary key,value pairs
            for key, value in data_dict.items():
                try:
                    writer.writerow([key.replace('"',''), value[0],value[1],value[2],value[3]])
            ### If value missing, 'NA'
                except IndexError:
                    writer.writerow([key.replace('"',''), value[0],value[1],value[2],'NA'])
        outputfile.close()
    
if __name__=='__main__':
    main()