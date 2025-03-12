import bcrypt
from pymongo import MongoClient

# Step 1: Connect to MongoDB
client = MongoClient("mongodb://127.0.0.1:27017/")  # Connect to your local MongoDB server
db = client["myDatabase"]  # Select the database
collection = db["myCollection"]  # Select the collection

# Step 2: Define the username and password (for example, "JohnDoe" and "mySecurePassword123")
username = "JohnDoe"
password = "mySecurePassword123"  # The password entered by the user

# Step 3: Hash the password using bcrypt
hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# Step 4: Create a dictionary to insert into MongoDB
user_data = {
    "username": username,
    "password": hashed_password  # Store the hashed password
}

# Step 5: Insert the user data into MongoDB
collection.insert_one(user_data)

print("User saved successfully.")
