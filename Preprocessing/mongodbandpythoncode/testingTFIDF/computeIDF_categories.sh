#!/usr/bin/sh
reviewcount=`grep -c -Eai "\ $1\ " RandomSampleOutputforTask1new.csv`
echo $reviewcount
