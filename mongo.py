'''
Connect to the mongoDB
'''
import pymongo
from pymongo import MongoClient
from collection import *

listof = []
listof = findall()
print "Printing list of file names:"
print listof

#assign them ids
ids=assignids(listof)
print ''
print "Printing id:filename pairs"
print ids

# def connect_to_db(name):
client = MongoClient('localhost', 27017)
db = client['tfidf']
collection = db['files']


for data in ids:
	collection.save(data)
# print post_id
print ''
print collection.find_one({"1": "first.txt"})
db.drop_collection(collection)
# post_id