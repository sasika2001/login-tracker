from tkinter import *
from tkinter import messagebox

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Window")
        self.root.geometry("400x300")
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
        
        # Predefined correct credentials (you can replace these with your actual logic)
        correct_username = "admin"
        correct_password = "password123"
        
        # Check if the username and password are correct
        if username != correct_username or password != correct_password:
            messagebox.showerror("Login Error", "Incorrect username or password!")
        else:
            print(f"Login successful!\nUsername: {username}\nPassword: {password}")
            # Here you can proceed to the next steps after a successful login.

root = Tk()
obj = Login(root)
root.mainloop()
