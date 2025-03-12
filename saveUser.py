import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["user_db"]  # Database
users_collection = db["users"]  # Collection

# Define 3 users with usernames and passwords
users = [
    {"username": "admin", "password": "admin123"},
    {"username": "user1", "password": "pass123"},
    {"username": "user2", "password": "mypassword"}
]

# Insert users into the database if they don’t exist already
for user in users:
    if not users_collection.find_one({"username": user["username"]}):
        users_collection.insert_one(user)
        print(f"User '{user['username']}' added to the database.")
    else:
        print(f"User '{user['username']}' already exists.")

print("User data setup completed!")
