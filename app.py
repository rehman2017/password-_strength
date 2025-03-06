import tkinter as tk
from tkinter import messagebox
import re

# Function to check password strength
def check_password_strength(password):
    # Checking for various strength criteria
    if len(password) < 8:
        return "Weak"
    elif len(password) < 12:
        if not re.search("[A-Za-z]", password) or not re.search("[0-9]", password):
            return "Medium"
        return "Good"
    else:
        if (re.search("[A-Za-z]", password) and 
            re.search("[0-9]", password) and 
            re.search("[!@#$%^&*(),.?\":{}|<>]", password)):
            return "Strong"
        return "Good"

# Function to update UI with password strength
def update_password_strength():
    password = password_entry.get()
    strength = check_password_strength(password)
    
    if strength == "Weak":
        strength_label.config(text="Weak", fg="red")
        strength_meter.config(bg="red")
    elif strength == "Medium":
        strength_label.config(text="Medium", fg="orange")
        strength_meter.config(bg="orange")
    elif strength == "Good":
        strength_label.config(text="Good", fg="yellow")
        strength_meter.config(bg="yellow")
    elif strength == "Strong":
        strength_label.config(text="Strong", fg="green")
        strength_meter.config(bg="green")

# Function to handle password submission
def submit_password():
    password = password_entry.get()
    if not password:
        messagebox.showwarning("Input Error", "Please enter a password!")
    else:
        strength = check_password_strength(password)
        messagebox.showinfo("Password Strength", f"Your password is: {strength}")

# Creating the main window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x300")
root.resizable(False, False)

# Style for labels and entry
root.config(bg="#2C3E50")

# Password label and entry box
password_label = tk.Label(root, text="Enter Password:", font=("Helvetica", 14), fg="white", bg="#2C3E50")
password_label.pack(pady=20)

password_entry = tk.Entry(root, font=("Helvetica", 14), show="*", width=30, bd=2, relief="solid")
password_entry.pack(pady=10)

# Password strength label and meter
strength_label = tk.Label(root, text="Strength", font=("Helvetica", 14), fg="white", bg="#2C3E50")
strength_label.pack(pady=5)

strength_meter = tk.Frame(root, height=10, width=300, bg="gray", relief="solid")
strength_meter.pack(pady=5)

# Button to check strength
check_button = tk.Button(root, text="Check Strength", font=("Helvetica", 14), bg="#3498DB", fg="white", command=update_password_strength)
check_button.pack(pady=20)

# Button to submit password
submit_button = tk.Button(root, text="Submit", font=("Helvetica", 14), bg="#1ABC9C", fg="white", command=submit_password)
submit_button.pack(pady=10)

# Running the application
root.mainloop()
