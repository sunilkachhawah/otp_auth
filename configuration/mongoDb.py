from pymongo import MongoClient, ASCENDING, IndexModel
# Set up MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["temp_otp_data"]
collection = db["dumpdata"]

ttl_index = IndexModel([("created_at", ASCENDING)], expireAfterSeconds=100)
# Create the TTL index on the collection
collection.create_indexes([ttl_index])

