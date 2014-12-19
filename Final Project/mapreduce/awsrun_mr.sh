#!/bin/bash

#Run create_job_flow.sh first to get the job-flow-id

for i in {1990..2013}
  do
    for t in {employment,weeklywage,establishments,totalwage}
      do
          folder=$i".q1-q4.by_industry"
         #mkdir $i
          python mr_weeklywage.py -c mrjob.conf -r emr --emr-job-flow-id=j-1WRO6X9MSGBQT  s3://mhayes/$folder/*csv > $i/$i"_weeklywage.txt"     
    done
done
