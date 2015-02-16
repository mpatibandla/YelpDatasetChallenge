#!/usr/bin/sh
# not used in this project just for testing lucene TF IDF code
reviewcount2=`grep -c -Eai "\ $1\ " RandomSampleOutputforTask1new.csv`
echo $reviewcount2
