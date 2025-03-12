from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymongo
from datetime import datetime
import socket

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        self.root.configure(bg="#f4f4f4")  # Light grey background

        # MongoDB Setup for user credentials
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.user_db = self.client["user_db"]  # Database for storing usernames and passwords
        self.users_collection = self.user_db["users"]  # Collection for user credentials
        
        # MongoDB Setup for login history
        self.login_db = self.client["login_db"]  # Database for login details
        self.login_history_collection = self.login_db["login_history"]  # Collection for login history
        
        self.create_widgets()

    def create_widgets(self):
        # Title Label
        self.title_label = Label(self.root, text="User Login", font=("Arial", 16, "bold"), bg="#f4f4f4")
        self.title_label.pack(pady=10)

        # Create Frame for Inputs
        frame = Frame(self.root, bg="white", padx=20, pady=20, relief=RIDGE, borderwidth=2)
        frame.pack(pady=20)

        # Username Label & Entry
        Label(frame, text="Username", font=("Arial", 12), bg="white").grid(row=0, column=0, pady=5, sticky=W)
        self.username_entry = ttk.Entry(frame, width=25, font=("Arial", 10))
        self.username_entry.grid(row=0, column=1, pady=5, padx=10)

        # Password Label & Entry
        Label(frame, text="Password", font=("Arial", 12), bg="white").grid(row=1, column=0, pady=5, sticky=W)
        self.password_entry = ttk.Entry(frame, width=25, font=("Arial", 10), show="*")
        self.password_entry.grid(row=1, column=1, pady=5, padx=10)

        # Login Button
        self.login_button = ttk.Button(self.root, text="Login", command=self.login_action)
        self.login_button.pack(pady=10)

    def login_action(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        # Validation for empty fields
        if not username and not password:
            messagebox.showerror("Input Error", "Username and Password cannot be empty!")
            return
        elif not username:
            messagebox.showerror("Input Error", "Please enter your Username!")
            return
        elif not password:
            messagebox.showerror("Input Error", "Please enter your Password!")
            return

        # Check credentials in MongoDB (user_db)
        user = self.users_collection.find_one({"username": username})

        # Get login details (IP address, current date/time)
        ip_address = socket.gethostbyname(socket.gethostname())
        login_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Log login attempt (in login_db)
        login_attempt = {
            "username": username,
            "ip_address": ip_address,
            "login_time": login_time,
            "status": "failed" if user is None or user["password"] != password else "success"
        }
        self.login_history_collection.insert_one(login_attempt)

        # Print login details to console
        print(f"Login Attempt Details:\nUsername: {username}\nIP Address: {ip_address}\nLogin Time: {login_time}\nStatus: {login_attempt['status']}\n")

        # Check if user exists and password matches
        if user is None:
            messagebox.showerror("Login Error", "Username not found!")
        elif user["password"] != password:
            messagebox.showerror("Login Error", "Incorrect password!")
        else:
            messagebox.showinfo("Login Successful", f"Welcome, {username}!")
            print(f"Login successful!\nUsername: {username}\nPassword: {password}")

# Run Application
root = Tk()
Login(root)
root.mainloop()
