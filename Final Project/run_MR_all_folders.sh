#!/bin/bash
for i in {1990..2014}
  do
     folder=$i".q1-q4.by_industry"
 #    mkdir $i
     python Yearly_Emloyment_Level_Mapreduce.py -c mrjob.conf -r emr --emr-job-flow-id=j-3JG6A8B8ZAYU6  s3://samuelkahn/BLS/$folder/*csv > $i/$i"_employment_level.txt"     
 done
