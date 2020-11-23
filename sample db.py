import pymongo
from pymongo import MongoClient

cluster = MongoClient('mongodb+srv://User:abcd1234@clusterdb.1f5hl.mongodb.net/Events?retryWrites=true&w=majority')
db = cluster["Events"]
collection = db["EventReported"]

post1 = {"_id": 1, "name": "trump", "score": 5}
post2 = {"_id": 2, "name": "Melanie", "score": 10}
collection.insert_many([post1, post2])
