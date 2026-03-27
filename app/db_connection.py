import os
from dotenv import load_dotenv
from pymongo import MongoClient

# --------------------------
# MongoDB connection
# --------------------------
load_dotenv("stack.env")
MONGO_USER = os.environ.get("MONGO_USER")
MONGO_PASS = os.environ.get("MONGO_PASS")
MONGO_HOST = os.environ.get("MONGO_HOST")
MONGO_PORT = os.environ.get("MONGO_PORT")
DATABASE_NAME = os.environ.get("DATABASE_NAME")

client = MongoClient(f"mongodb://{MONGO_USER}:{MONGO_PASS}@{MONGO_HOST}:{MONGO_PORT}/")
db = client[DATABASE_NAME]