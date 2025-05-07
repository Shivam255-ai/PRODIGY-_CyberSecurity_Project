import tkinter as tk
import re
import random
import string
from tkinter import messagebox

# Function to check password strength
def check_strength():
    password = password_entry.get()
    strength = 0
    feedback = []

    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters.")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    if re.search(r"[0-9]", password):
        strength += 1
    else:
        feedback.append("Add at least one number.")

    if re.search(r"[\W_]", password):
        strength += 1
    else:
        feedback.append("Add at least one special character (e.g., @, #, $, etc.).")

    if strength == 5:
        result_label.config(text="Strong Password 🔒", fg="green")
    elif 3 <= strength < 5:
        result_label.config(text="Moderate Password ⚠️", fg="orange")
    else:
        result_label.config(text="Weak Password ❌", fg="red")

    feedback_text.set("\n".join(feedback) if feedback else "Excellent password!")

# Function to generate random strong password
def generate_password():
    try:
        length = int(length_entry.get())
        if length < 8:
            messagebox.showerror("Error", "Password length should be at least 8.")
            return
        chars = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(chars) for _ in range(length))
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
        result_label.config(text="Generated Password ✅", fg="blue")
        feedback_text.set("Click 'Check Strength' to evaluate.")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer for length.")

# Function to copy password to clipboard
def copy_to_clipboard():
    password = password_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

# GUI Setup
root = tk.Tk()
root.title("Password Strength Checker + Generator")
root.geometry("500x400")
root.resizable(False, False)

tk.Label(root, text="Enter a password:", font=("Arial", 12)).pack(pady=5)
password_entry = tk.Entry(root, width=40, font=("Arial", 12), show="*")
password_entry.pack(pady=5)

tk.Button(root, text="Check Strength", command=check_strength, bg="lightblue", width=20).pack(pady=5)
tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, bg="lightgreen", width=20).pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
result_label.pack(pady=5)

feedback_text = tk.StringVar()
tk.Label(root, textvariable=feedback_text, font=("Arial", 10), fg="gray", wraplength=400, justify="left").pack(pady=5)

# Password Generator Section
tk.Label(root, text="--- Generate a Strong Password ---", font=("Arial", 11, "bold")).pack(pady=10)
tk.Label(root, text="Enter desired length:", font=("Arial", 10)).pack()
length_entry = tk.Entry(root)
length_entry.pack(pady=3)
length_entry.insert(0, "12")

tk.Button(root, text="Generate Password", command=generate_password, bg="orange", width=20).pack(pady=5)

root.mainloop()
