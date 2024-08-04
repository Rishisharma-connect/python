from pymongo import MongoClient
from bson import json_util


MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
connection = MongoClient(MONGODB_HOST, MONGODB_PORT)

mydb = connection["mydatabase"]
mycol = mydb["customers"]

mydict = { "name": "John", "address": "Highway 37" }

x = mycol.insert_one(mydict)

print(connection.list_database_names())

print(mydb.list_collection_names())

x = mycol.find_one()

print(x)



