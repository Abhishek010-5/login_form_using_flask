from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

db_uri = os.getenv("URI")
db = os.getenv("DB")

def get_database():
    client = MongoClient(db_uri, serverSelectionTimeoutMS=5000)
    return client[db]
