from pymongo import MongoClient
from bson import json_util


MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
connection = MongoClient(MONGODB_HOST, MONGODB_PORT)

