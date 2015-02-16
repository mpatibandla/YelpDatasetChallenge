#/usr/bin/python
import os
import csv
import re
import sys
import subprocess
import operator
import numpy as np


for line in open('reviewsinformation_task2.csv','r'):
	scores=dict()
	#print line
	count=dict();
	for word in line.split():
		if count.has_key(word):
			count[word] = count[word] + 1
		else:
			count[word]=1

	for word in line.split():
		if scores.has_key(word):
			continue	
		tf  = count.get(word)
		idftemp = int(subprocess.check_output(["sh","computeIDF.sh",word],stderr=subprocess.STDOUT))
		#print "tf for word ",word,"is ",tf,"idf is ",idftemp
		if idftemp == 0:
			score = 0
		else:
			idf = 1 / np.float64(idftemp)
			#print "tf for word ",word,"is ",tf,"idf is ",idf
			score = np.float64(tf * idf)
		scores[word]= score
		print "score for word ", word ," is : ",scores.get(word) 
	sorted_x = sorted(scores.items(), key=operator.itemgetter(1),reverse=True)	
        sorted_list = [i[0] for i in sorted_x] 
        print ' '.join(sorted_list[:10])
        print ' '.join(sorted_list[:10])



