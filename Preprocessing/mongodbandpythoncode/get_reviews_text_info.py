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



def get_reviews_without_Stopwords():
    print " inside reviews json to get non nouns from reviews and without stop words"
    collection = db.reviews
    f = open('Reviewsinformation_WithoutStopWords.csv','w')
    f2 = open('Reviewsinformation_Without_Nouns.csv','w')
    f3 = open('Reviewsinformation_OnlyAdjectives.csv','w')
    count=0    # Get all stop words
    stop = stopwords.words('english')
    for lines in open('reviewsinformation_task2.csv','r'):
        line=lines.split(',')
        # 0 - business id, 1 - text , 2 - rating 
        words=[] 
        #print reviews['text']
        # careful unicode should have unicode string as input . Trash any special charecters if unicode can not convert them
        temp        = unicodedata.normalize('NFKD',line[1]).encode('ascii','ignore')
        text        = re.sub(r"[^\w  ]",' ',temp.lower())    
        for word in text.split():
            if word not in stop:
                #print word,'\n'
                words.append(word.lower())
        tagged_sent = pos_tag(text.split())
        nonnouns=[]
        adjectives=[]
        for word,pos in tagged_sent:
            if pos.find("NN")== -1: # other than nouns
                nonnouns.append(word.lower())
            if pos.find("JJ") != -1 : # only adjectives
                adjectives.append(word.lower())

        businessid  = line[0]
        f.write(businessid+','+' '.join(words) + ',' +  str(line[2])+  '\n')
        f2.write(businessid+','+' '.join(nonnouns)+ ',' +  str(line[2]) + '\n')
        f3.write(businessid+','+' '.join(adjectives)+ ',' +  str(line[2])+ '\n')
        count = count + 1
        print " reviews read count ",count
    print "total review word count ",count
    f.close()
    f2.close()
    f3.close()
        




def get_categories():
    print "\n Inside Categories "
    collection = db.business
    f = open('categoryinformation_with_only_Nouns.csv','w')
    f2 = open('categoryinformation_WithoutStopwords.csv','w')
    count=0
    print "getting categories only nouns"
    for lines in open('categoryinformation_task1.csv','r'):
        line=lines.split(',')
        # careful unicode should have unicode string as input . Trash any special charecters if unicode can not convert them
        temp         = unicodedata.normalize('NFKD',line[1]).encode('ascii','ignore')
        text         = re.sub(r"[^\w  ]",' ',temp.lower())
        #nonstop = []
        nonstop = [ word_text for word2 in text if word2 not in stop]
        tagged_sent  = pos_tag(text.split())
        nouns        = [word for word,pos in tagged_sent if pos.find("NN") != -1]
        businessid   = line[0]
        reviewid     = line[2]
        f.write(businessid+','+' '.join(nouns)+','+str(categories) + ',' + reviewid +'\n')
        f2.write(businessid+','+' '.join(nonstopwords)+','+str(categories) + ',' + reviewid +'\n')
    print "total count" ,count
    f.close()
    f2.close()



get_reviews_without_Stopwords()

print "\n writing categories done with reviews :)) \n\n"

get_categories()


