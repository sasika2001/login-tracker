from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv() #load environment variable from the .env file

MONGO_URL=os.getenv("MONGO_URL") #get mongodb connection string from environment variable

client=MongoClient(MONGO_URL) #establish connection to mongodb
db=client["login_tracker_db"] #database name 
logins_collection=db["logins"] #collection name for storing login data 