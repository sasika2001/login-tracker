import tkinter as tk
from tkinter import messagebox
import bcrypt
from pymongo import MongoClient

# Step 1: Connect to MongoDB
client = MongoClient("mongodb://127.0.0.1:27017/")  # Connect to your local MongoDB server
db = client["myDatabase"]  # Select the database
collection = db["myCollection"]  # Select the collection

# Step 2: Define the function to handle login
def login():
    # Get entered username and password from the GUI input fields
    entered_username = entry_username.get()
    entered_password = entry_password.get()

    # Step 3: Fetch the stored user data from MongoDB
    user_data = collection.find_one({"username": entered_username})

    if user_data:
        # Step 4: Get the stored hashed password from MongoDB
        stored_hashed_password = user_data["password"]

        # Step 5: Check if the entered password matches the stored hashed password
        if bcrypt.checkpw(entered_password.encode('utf-8'), stored_hashed_password):
            messagebox.showinfo("Login Status", "Login successful!")
        else:
            messagebox.showerror("Login Status", "Incorrect password.")
    else:
        messagebox.showerror("Login Status", "Username not found.")

# Step 6: Create the main window
window = tk.Tk()
window.title("Login")
window.geometry("400x300")  # Window size (width x height)
window.config(bg="#2c3e50")  # Set background color

# Step 7: Create a frame for a cleaner layout
frame = tk.Frame(window, bg="#34495e", padx=20, pady=20)
frame.pack(padx=40, pady=40)

# Step 8: Add labels and entry fields with custom fonts and colors
label_username = tk.Label(frame, text="Username", font=("Arial", 14), fg="white", bg="#34495e")
label_username.grid(row=0, column=0, pady=10, sticky="w")

entry_username = tk.Entry(frame, font=("Arial", 14), width=20)
entry_username.grid(row=0, column=1, pady=10)

label_password = tk.Label(frame, text="Password", font=("Arial", 14), fg="white", bg="#34495e")
label_password.grid(row=1, column=0, pady=10, sticky="w")

entry_password = tk.Entry(frame, font=("Arial", 14), show="*", width=20)
entry_password.grid(row=1, column=1, pady=10)

# Step 9: Create a login button with custom style
login_button = tk.Button(frame, text="Login", font=("Arial", 14), bg="#2980b9", fg="white", command=login, width=15)
login_button.grid(row=2, columnspan=2, pady=20)

# Step 10: Create a sign-up link (if necessary) for user registration
signup_label = tk.Label(frame, text="Don't have an account? Sign Up", font=("Arial", 10), fg="#ecf0f1", bg="#34495e", cursor="hand2")
signup_label.grid(row=3, columnspan=2)
signup_label.bind("<Button-1>", lambda e: messagebox.showinfo("Sign Up", "Sign up functionality here."))

# Step 11: Start the Tkinter event loop
window.mainloop()
