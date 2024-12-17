import tkinter as tk
from tkinter import messagebox
from modules.hash_password import hash_password
from modules.password_policy import check_password_policy
from modules.encrypt_password import generate_key, encrypt_password, decrypt_password

def hash_password_action():
    password = entry_password.get()
    hashed = hash_password(password)
    messagebox.showinfo("SHA-256 Hashed Password", hashed)

def check_policy_action():
    password = entry_password.get()
    result = check_password_policy(password)
    messagebox.showinfo("Password Policy Result", result)

def encrypt_password_action():
    key = generate_key()
    password = entry_password.get()
    encrypted = encrypt_password(key, password)
    messagebox.showinfo("Encryption Results", f"Key: {key.decode()}\nEncrypted: {encrypted.decode()}")

# Build the GUI
root = tk.Tk()
root.title("Password Cracking & Protection Toolkit")
root.geometry("400x400")
root.configure(bg="#2C3E50")

# Title Label
tk.Label(root, text="Password Toolkit", font=("Arial", 16, "bold"), fg="white", bg="#2C3E50").pack(pady=10)

# Input Field
tk.Label(root, text="Enter Password:", font=("Arial", 12), fg="white", bg="#2C3E50").pack(pady=5)
entry_password = tk.Entry(root, show="*", font=("Arial", 12), width=30)
entry_password.pack(pady=5)

# Buttons
tk.Button(root, text="Hash Password", command=hash_password_action, bg="#3498DB", fg="white", font=("Arial", 12)).pack(pady=5)
tk.Button(root, text="Check Password Policy", command=check_policy_action, bg="#E67E22", fg="white", font=("Arial", 12)).pack(pady=5)
tk.Button(root, text="Encrypt Password", command=encrypt_password_action, bg="#27AE60", fg="white", font=("Arial", 12)).pack(pady=5)

# Exit Button
tk.Button(root, text="Exit", command=root.destroy, bg="red", fg="white", font=("Arial", 12)).pack(pady=20)

root.mainloop()
