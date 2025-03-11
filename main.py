from fastapi import FastAPI
from pydantic import BaseModel
import os
from dotenv import load_dotenv
from pymongo import MongoClient
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

# MongoDB connection setup
MONGO_URL = os.getenv("MONGO_URL")
client = MongoClient(MONGO_URL)
db = client.get_database()  # Get the database from the URL
logins_collection = db["logins"]  # The collection where login data will be stored

app = FastAPI()

# Define a Pydantic model for login data
class LoginRequest(BaseModel):
    user_id: str
    ip_address: str

# Route to record login data
@app.post("/login")
async def record_login(login_request: LoginRequest):
    login_data = {
        "user_id": login_request.user_id,
        "timestamp": datetime.now(),
        "ip_address": login_request.ip_address
    }
    
    logins_collection.insert_one(login_data)  # Insert login data into MongoDB
    return {"message": "Login recorded successfully!"}

# Existing routes for testing MongoDB connection
@app.get("/")
def readRoot():
    return {"message": "Hello, this is MongoDB Atlas"}

@app.get("/status")
def checkStatus():
    try:
        client.server_info()
        return {"status": "Connected to MongoDB Atlas"}
    except Exception as e:
        return {"status": "Failed to connect", "error": str(e)}
