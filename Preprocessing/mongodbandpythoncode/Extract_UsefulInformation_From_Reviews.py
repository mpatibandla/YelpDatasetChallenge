#/usr/bin/python
import os
import pprint
import csv
import unicodedata
import re
import nltk
import sys
from nltk.corpus import stopwords
from nltk.tag import pos_tag
from nltk.stem import SnowballStemmer
# GEt information from reviews and apply stop word removal, parts of speech taggging and stemming on it
def get_reviews_without_Stopwords():
    print " Opening file reviewsinformation_task2.csv";
    print " inside reviews json to get non nouns from reviews and without stop words"
    f  = open('Reviewsinformation_WithoutStopWords.csv','w')
    f2 = open('Reviewsinformation_Without_Nouns.csv','w')
    f3 = open('Reviewsinformation_OnlyAdjectives.csv','w')
    f4 = open('Reviewsinformation_Stemmed.csv','w')
    count=0    # Get all stop words
    stop = stopwords.words('english')
    stemmer = SnowballStemmer("english") # stemmer to stem the words
    for lines in open('reviewsinformation_task2.csv','r'):
        line    =lines.split(',')
        # 0 - business id, 1 - text , 2 - rating
        words     =[]
        stemwords =[]
        text      =line[1]
        for word in text.split():
            # Appling stemming to each word  and append to stemwords list
            stemwords.append(stemmer.stem(word))
            if word not in stop:
                # Add non stop words to words list
                words.append(word.lower())
        # Part of speech tagging goes here
        tagged_sent = pos_tag(text.split())
        nonnouns=[]
        adjectives=[]
        for word,pos in tagged_sent:
            if pos.find("NN")== -1: # pick words other than nouns and add to nonnouns list
                nonnouns.append(word.lower())
            if pos.find("JJ") != -1 : # pick only adjectives and add to adjectives list
                adjectives.append(word.lower())

        businessid  = line[0]
        f.write(businessid +','+' '.join(words)+','+str(line[2]))
        f2.write(businessid+','+' '.join(nonnouns)+','+str(line[2]))
        f3.write(businessid+','+' '.join(adjectives)+','+str(line[2]))
        f4.write(businessid+','+' '.join(stemwords)+','+str(line[2]))
        count = count + 1
        print " reviews read count ",count
    print "total review word count ",count
    f.close()
    f2.close()
    f3.close()
    f4.close()

def get_categories():
    print "\n Inside Categories "
    f   = open('categoryinformation_with_only_Nouns.csv','w')
    f2  = open('categoryinformation_WithoutStopwords.csv','w')
    f3  = open('categoryinformation_stemmedwords.csv','w')
    count=0
    stemmer = SnowballStemmer("english")
    stop = stopwords.words('english')
    print "getting categories only nouns"
    for lines in open('categoryinformation_task1.csv','r'):
        line=lines.split(',')
        text         = line[1]
        nonstop      = [word2 for word2 in text.split() if word2 not in stop]
        tagged_sent  = pos_tag(text.split())
        # Appling stemming to each word  and append to stemwords list
        stemwords    = [stemmer.stem(stemmedword) for stemmedword in text.split()]
        # Get all nouns , find will return -1 if the pos is not NN. Noun will have NN as position values.
        nouns        = [word for word,pos in tagged_sent if pos.find("NN") != -1]
        businessid   = line[0]
        categories   = line[2]
        print "Categories line number processed ",count
        count        = count +1
        f.write(businessid+','+' '.join(nouns)+','+categories)
        f2.write(businessid+','+' '.join(nonstop)+','+categories)
        f3.write(businessid+','+' '.join(stemwords)+','+categories)
    print "total count" ,count
    f.close()
    f2.close()
    f3.close()

get_reviews_without_Stopwords()

print "\n writing categories done with reviews :)) \n\n"

get_categories()

print " \n End of script. Execution successful \n"
