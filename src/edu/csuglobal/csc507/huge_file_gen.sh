#!/bin/bash
for i in {1..1000}
do
  cat ./files/module8/file1.txt >> ./files/module8/hugefile1.txt
  cat ./files/module8/file2.txt >>./files/module8/hugefile2.txt
done