from pymongo import MongoClient
# Set up MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["mobile_numbers"]
collection = db["numbers"]
