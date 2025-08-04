from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get MongoDB URI from .env
uri = os.getenv("MONGO_DB_URL")

# Connect to MongoDB
client = MongoClient(uri)

try:
    client.admin.command('ping')
    print("✅ Connected to MongoDB from .env!")
except Exception as e:
    print("❌ MongoDB connection failed:", e)
