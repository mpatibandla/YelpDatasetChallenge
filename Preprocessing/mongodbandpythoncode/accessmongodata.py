import pymongo
import os
from pymongo import MongoClient
import codecs
import pprint
import csv
import unicodedata
import re
def setupMongo():
    client= MongoClient()
    db = client.yelpdata
    return db


def get_reviews(db):
    print " inside reviews"
    collection = db.reviews
    f = open('reviewsinformation_task2.csv','w')
    f2= open('reviewsinformation_deviated_forreference.csv','w');
    count=0
    # Get all stop words
    #stop = stopwords.words('english')
    # Get the reviews text and rating from business JSON
    for reviews in collection.find({},{'business_id':1,'text':1,'stars':1}):
        # careful unicode should have unicode string as input . Trash any special charecters if unicode can not convert them
        text = unicodedata.normalize('NFKD',reviews['text']).encode('ascii','ignore')
        #businessid= unicodedata.normalize('NFKD',reviews['business_id']).encode('ascii','ignore') 
        businessid=reviews['business_id']
        f.write( businessid +', "'+text + '" ,' +  str(reviews['stars']) + '\n')
        if len(businessid + text) != len(reviews['business_id'] + reviews['text']):
            f2.write(reviews['business_id'].encode('utf8')+',' + reviews['text'].encode('utf8')+ ',' +  str(reviews['stars']) + '\n')
        count = count + 1
        #print "count ",count
    print "total review count ",count
    f.close()
    f2.close()



def get_categories(db):
    collection = db.business
    f = open('reviewsinformation_task1.csv','w')
    f2= open('reviewsinformation_task1_deviated.csv','w')
    count=0
    print "getting categories"
    for business in collection.find({},{"business_id" :1,"categories":1}):
        for reviews in db.reviews.find({"business_id":business['business_id']},{"text":1,"business_id":1}):
            if (len(business['categories']) > 1):
                #print count
                temp = unicodedata.normalize('NFKD',reviews['text']).encode('ascii','ignore')
                review_text       = re.sub(r'[^\w -]','',temp)
                #businessid= unicodedata.normalize('NFKD',business['business_id']).encode('ascii','ignore')
                businessid = business['business_id']
                for categories in business['categories']:
                    if((len(business['business_id']) + len(reviews['text'])) != (len(businessid) + len(review_text))):
                        f2.write(business['business_id'].encode('utf8')+', "'+reviews['text'].encode('utf8')+'" ,'+str(categories)+'\n')
                    f.write(businessid+','+review_text+','+str(categories)+'\n')
                count=count + 1
    print "total count" ,count
    f.close()
    f2.close()



def get_onecategory_business(db):
    #categories=()
    collection = db.business
    f = open('business_with_singlecategories_task1.csv','w');
    f2 = open('business_with_singlecategories_task1_deviated_for_reference.csv','w');
    for business in collection.find({},{"business_id" :1,"categories":1}):
        for reviews in db.reviews.find({"business_id":business['business_id']},{"text":1,"business_id":1}):
            #businessid= unicodedata.normalize('NFKD',business['business_id']).encode('ascii','ignore')
            businessid = business['business_id']
            if (len(business['categories']) == 1):
                #review_text = reviews['text'].encode('utf8')
                review_text = unicodedata.normalize('NFKD',reviews['text']).encode('ascii','ignore')
                for categories in business['categories']:
                    if((len(business['business_id']) + len(reviews['text'])) != (len(businessid) + len(review_text))):
                        f2.write(business['business_id']+', "'+reviews['text'].encode('utf8')+'" ,'+str(categories)+'\n')
                    f.write(businessid+','+review_text+','+str(categories)+'\n')
    f.close()
    f2.close()







def get_business(db):
    f = open('businessid.csv','w')
    for business in db.business.find({},{"business_id":1,"_id":0}):
        f.write(business['business_id'] + '\n')
    f.close()




print os.getcwd();

os.chdir("C:\Users\giridhar\Desktop\Project\yelp_dataset_challenge_academic_dataset\Final Files\Required")

#print db.collection_names()

db=setupMongo()
get_business(db)
#validate_businessidfile(db)
# Creates a file required for task 1 for business where there are atleast two categories
get_categories(db)
# Creates a file required for task 2 . Review text and ratings are fetched from mongo collection into a file
#get_reviews(db)

# Creates a file required for task 1 for business where there are one categories . Need this file to test on completely new testing file with no features 
#get_onecategory_business(db)

print_businessid(db)


'''
categories=()


categories=get_categories(db)

pprint.pprint(categories)
    


Helper comments
collection = db.reviews
for review in collection.find({"business_id" : "vcNAWiLM4dR7D2nwwJ7nCA"},{'text':1,'stars':1}):
    review
'''
'''

def get_categories(db):
    categories=()
    collection = db.business
    f = open('reviewsinformation_task1_new2.txt','w')
    for business in collection.find({},{"business_id" :1,"categories":1}):
        for reviews in db.reviews.find({"business_id":business['business_id']},{"text":1,"business_id":1}):
            if (len(business['categories']) > 1):
                review_text = reviews['text'].encode('utf8')
                for categories in business['categories']:
                    f.write(business['business_id'].encode('utf8')+', "'+review_text+'" ,'+categories.encode('utf8')+'\n')
    #print 'end \n'
    #return categories
    f.close()



def get_onecategory_business(db):
    categories=()
    collection = db.business
    f = open('business_with_singlecategories_task1_new2.txt','w');
    for business in collection.find({},{"business_id" :1,"categories":1}):
        for reviews in db.reviews.find({"business_id":business['business_id']},{"text":1,"business_id":1}):
            if (len(business['categories']) == 1):
                review_text = reviews['text'].encode('utf8')
                for categories in business['categories']:
                    f.write(unicodedata.normalize('NFKD',business['business_id']).encode('utf8')+', "'+review_text+'" ,'+unicodedata.normalize('NFKD',categories).encode('utf8')+'\n')
    f.close()


def validate_businessidfile(db):
    collection = db.business
    print "\n inside vali"
    f = open('businessid.csv','r')
    f2= open('businessidmissed.csv','w')
    for line in f:
        for business in db.business.find({"business_id":line},{"business_id":1}):
            if(business['business_id'] != line):
                f2.write(line +'\t'+business['business_id'] +'\n')
    print "\n end of loops"
    f.close()
    f2.close()
'''

'''
def get_business(db):
    collection = db.business
    #print collection.find_one({},{'text':1,'stars':1}) 
    count=0
    f  = open('businessid.csv','wb')
    f2 = open('businessid_old.csv','wb')
    #filewriter=csv.writer(f, delimiter = '|',quotechar='|', quoting=csv.QUOTE_MINIMAL);
    print "created file businses id " 
    collection = db.business
    for business in collection.find({},{"business_id" :1}):
        # careful unicode should have unicode string as input. Trash any special charecters if unicode can not convert them
        temp             = unicodedata.normalize('NFKD',business['business_id']).encode('ascii','ignore')
        f2.write(temp+'\n')
        #businessid       = re.sub(r'[^\w-]','',temp)
        #businessid = unicodedata.normalize('NFKD',temp).encode('ascii','ignore')
        #filewriter.writerow(businessid)
        f.write(businessid+'\n')
        count = count +1
    print "total business identifiers ",count
    f.close()
'''



