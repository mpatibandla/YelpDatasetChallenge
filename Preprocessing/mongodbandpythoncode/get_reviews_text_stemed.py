import pymongo
import os
from pymongo import MongoClient
import pprint
import csv
import unicodedata
import re
import nltk
from nltk.corpus import stopwords
from nltk.tag import pos_tag
from nltk.stem import SnowballStemmer
stemmer = SnowballStemmer("english")

def get_reviews_stemmed():
    #print " inside reviews json to get non nouns from reviews and without stop words"
    f = open('Reviewsinformation_stemmed.csv','w')
    count=0    # Get all stop words
    stop = stopwords.words('english')
    for lines in open('reviewsinformation_task2.csv','r'):
        line=lines.split(',')
        # 0 - business id, 1 - text , 2 - rating 
        words=[] 
        text =line[1]   
	# Stemming on the keywords present in the reviews
        for word in text.split():
            words.append(stemmer.stem(word))
        businessid  = line[0]
        f.write(businessid+','+' '.join(words) + ',' +  str(line[2])+  '\n')
        count = count + 1
        print " reviews read count ",count
    print "total review word count ",count
    f.close()

        

def get_categories_stemmed():
    print "\n Inside Categories "
    f = open('categoryinformation_stemmed.csv','w')
    count=0
    print "getting categories only nouns"
    for lines in open('categoryinformation_task1.csv','r'):
        line=lines.split(',')
        # careful unicode should have unicode string as input . Trash any special charecters if unicode can not convert them
        words=[]
        text= line[1]
	# Stemming on the keywords present in the reviews
        for word in text.split():
            words.append(stemmer.stem(word))
        businessid   = line[0]
        reviewid     = line[2]
        f.write(businessid+','+' '.join(words)+','+str(categories) + ',' + reviewid +'\n')
    print "total count" ,count
    f.close()
    f2.close()


# call the functions dont forget :)
get_reviews_stemmed()

print "\n writing categories done with reviews :)) \n\n"

get_categories_stemmed()


