import pymongo
from pymongo import MongoClient, ASCENDING, IndexModel
# Set up MongoDB connection
client = MongoClient("mongodb://localhost:27017")
db = client["temp_otp_data"]
collection = db["dumpdata"]
# Create a TTL index for automatic deletion after 5 minutes
ttl_index = IndexModel([("time", ASCENDING)], expireAfterSeconds=300)
collection.create_indexes([ttl_index])


