#!/bin/bash
for i in {1990..2014}
  do
     folder=$i
     cd $i
     rm $i"empllevel_output.txt"
     cd ../
 done
