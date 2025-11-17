from motor.motor_asyncio import AsyncIOMotorClient
from typing import AsyncGenerator
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URL = os.getenv(
    "MONGO_URL",
    "mongodb+srv://ritwikzz14_db_user:NS8y42DXfBuGZeG5@cluster1.p65uqoa.mongodb.net/?retryWrites=true&w=majority"
)

client = AsyncIOMotorClient(MONGO_URL)
db = client["user_service"]

def get_user_collection():
    return db["users"]