from pymongo import MongoClient
from api.config import DB, DB_URI

def get_database():
    client = MongoClient(DB_URI, serverSelectionTimeoutMS=5000)
    return client[DB]
