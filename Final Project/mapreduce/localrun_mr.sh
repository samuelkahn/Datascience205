#!/bin/bash
for i in {1990..2013}
  do
    for t in {employment,weeklywage,establishments,totalwage}
      do
          folder=$i".q1-q4.by_industry"
         #mkdir $i
          python mr_$t.py  /media/matt/Data/Downloads/BLS/$folder/*csv > $i/$i"_"$t"_local.txt"
    done
done
