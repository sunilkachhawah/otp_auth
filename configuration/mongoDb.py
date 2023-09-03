import pymongo
from pymongo import MongoClient, ASCENDING, IndexModel
# Set up MongoDB connection
client = MongoClient("mongodb://localhost:27017")
db = client["temp_otp_data"]
collection = db["dumpdata"]
collection.create_index([("expireAt", ASCENDING)], expireAfterSeconds=0)


