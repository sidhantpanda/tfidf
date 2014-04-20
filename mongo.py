'''
Connect to the mongoDB
'''
import pymongo
from pymongo import MongoClient
from collection import *

# def connect_to_db(port,database):
client = MongoClient('localhost', 27017)
db = client['tfidf']
collection = db['files']