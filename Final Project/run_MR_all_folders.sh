#!/bin/bash
for i in {2010..2014}
  do
     folder=$i".q1-q4.by_industry"
     mkdir $i
     python Average_Income_MapReduce.py -c mrjob.conf -r emr --emr-job-flow-id=j-3595L8HT3BGN5  s3://samuelkahn/BLS/$folder/*csv > $i/$i"_output.txt" 
 done
