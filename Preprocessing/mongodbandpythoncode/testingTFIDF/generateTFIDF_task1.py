#/usr/bin/python
import os
import csv
import re
import sys
import subprocess
import operator
import numpy as np

print "\n opening file categoryinformation_task1.csv\n"
counter=1

for line in open('RandomSampleOutputforTask1new.csv','r'):
        f  = open('categoryinformation_top10.csv','w')
        f2 = open('categoryinformation_top20.csv','w')
        f3 = open('categoryinformation_top30.csv','w')	
	data =line.split(",")
	scores=dict()
	#print line
	count=dict();
	text=data[1]
	# Compute count hash map for each word ( Used to get TF of each word)
	for word in text.split():
		if count.has_key(word):
			count[word] = count[word] + 1
		else:
			count[word]=1

	for word in text.split():
		if scores.has_key(word):
			continue	
		tf  = count.get(word)
		# Shell script will give the IDF of the word
		idftemp = int(subprocess.check_output(["sh","computeIDF_categories.sh",word],stderr=subprocess.STDOUT))
		#print "tf for word ",word,"is ",tf,"idf is ",idftemp
		if idftemp == 0 and idftemp:
			score = 0
		else:
			idf = 1 / np.float64(idftemp)
			#print "tf for word ",word,"is ",tf,"idf is ",idf
			score = np.float64(tf * idf)
		scores[word]= score
		#print "score for word ", word ," is : ",scores.get(word) 
	sorted_x = sorted(scores.items(), key=operator.itemgetter(1),reverse=True)	
        sorted_list = [i[0] for i in sorted_x] 
	businessid   = data[0]
        categories   = data[2]
        print "Categories line number processed ",counter
        counter        = counter +1
        f.write(businessid+','+' '.join(sorted_list[:10])+','+categories)
        f2.write(businessid+','+' '.join(sorted_list[:20])+','+categories)
        f3.write(businessid+','+' '.join(sorted_list[:30])+','+categories)

f.close()
f2.close()
f3.close()


