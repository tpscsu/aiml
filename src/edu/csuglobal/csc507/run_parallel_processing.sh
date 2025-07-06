#!/bin/bash

cd ./files/module8/ || exit 1

start=$(date +%s)
echo "Starting parallel processing..."

for i in $(seq -w 0 9); do
  python3 ../../process_pair.py hugefile1_part_0${i}.txt hugefile2_part_0${i}.txt total_part_${i}.txt &
done


wait

cat total_part_*.txt > totalfile.txt

end=$(date +%s)
duration=$((end - start))

echo "Parallel processing complete."
echo "Time taken: ${duration} seconds"
