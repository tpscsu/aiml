#!/bin/bash

SECONDS=0

> newfile1.txt
while read -r number
do
  let "number *= 2"
  echo $number >> newfile1.txt
done < file1.txt

duration=$SECONDS
echo "Execution time: $duration seconds"