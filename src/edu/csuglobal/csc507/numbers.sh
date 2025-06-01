#!/bin/bash

echo "Start time: $(date)"
start=$SECONDS

> file1.txt
for ((i=0; i<1000000; i++)); do
  echo $RANDOM >> file1.txt
done

duration=$(( SECONDS - start ))
echo "End time: $(date)"
echo "Total time: $duration seconds"
