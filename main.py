from tkinter import *
from tkinter import messagebox
import pymongo

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Window")
        self.root.geometry("400x300")
        
        # MongoDB Setup
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")  # Connect to local MongoDB server
        self.db = self.client["user_db"]  # Create/select the database
        self.users_collection = self.db["users"]  # Create/select the collection for user data
        
        self.create_widgets()
    
    def create_widgets(self):
        # Username Label and Entry
        self.username_label = Label(self.root, text="Username")
        self.username_label.pack(pady=10)
        
        self.username_entry = Entry(self.root)
        self.username_entry.pack(pady=10)
        
        # Password Label and Entry
        self.password_label = Label(self.root, text="Password")
        self.password_label.pack(pady=10)
        
        self.password_entry = Entry(self.root, show="*")  # 'show' hides the password input
        self.password_entry.pack(pady=10)
        
        # Login Button
        self.login_button = Button(self.root, text="Login", command=self.login_action)
        self.login_button.pack(pady=20)
    
    def login_action(self):
        # Get the username and password values
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Check if the username or password is empty
        if not username or not password:
            messagebox.showerror("Input Error", "Please fill in both fields!")
            return
        
        # Check if the entered username and password match the stored values in MongoDB
        user = self.users_collection.find_one({"username": username})
        
        if user is None:
            messagebox.showerror("Login Error", "Username not found!")
        elif user["password"] != password:
            messagebox.showerror("Login Error", "Incorrect password!")
        else:
            print(f"Login successful!\nUsername: {username}\nPassword: {password}")
            # Proceed with the next steps (e.g., opening a new window)

    def create_test_user(self):
        # Create a test user (only run this once to create the user in the database)
        self.users_collection.insert_one({
            "username": "admin",
            "password": "password123"
        })
        print("Test user created in the database.")

root = Tk()
obj = Login(root)

# To create a test user (only once), uncomment the following line
# obj.create_test_user()

root.mainloop()
