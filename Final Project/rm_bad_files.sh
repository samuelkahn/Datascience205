#!/bin/bash
for i in {1990..2014}
  do
     cd $i
     rm $i"_mapreduce_aggregate.csv"
     rm $i"_contributions.txt"
     cd ..
done
