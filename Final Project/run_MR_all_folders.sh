#!/bin/bash
for i in {1990..2013}
  do
     folder=$i".q1-q4.by_industry"
 #    mkdir $i
     python Contributions_MapReduce.py -c mrjob.conf -r emr --emr-job-flow-id=j-1Y205MR4DFNG2  s3://samuelkahn/BLS/$folder/*csv > $i/$i"_contributions.txt"     
done
python Contributions_MapReduce.py -c mrjob.conf -r emr --emr-job-flow-id=j-1Y205MR4DFNG2  s3://samuelkahn/BLS/2014.q1-q1.by_industry/*csv > 2014/2014_contributions.txt     
