#!/bin/bash
for i in {1990..2014}
  do
     folder=$i".q1-q4.by_industry"
     mkdir $i
     python Average_Income_MapReduce.py -c mrjob.conf -r emr --emr-job-flow-id=j-2P4NY3QYBMDLZ  s3://samuelkahn/BLS/$folder/*csv > $i/$i"_output.txt" 
 done
