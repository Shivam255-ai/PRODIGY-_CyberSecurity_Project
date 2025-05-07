import tkinter as tk
from tkinter import messagebox

# Caesar Cipher encryption
def caesar_encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted += char
    return encrypted

# Caesar Cipher decryption
def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# Encrypt button callback
def encrypt_text():
    try:
        shift = int(shift_entry.get())
        message = message_entry.get("1.0", tk.END).strip()
        encrypted = caesar_encrypt(message, shift)
        output_text.set(f"Encrypted Message:\n{encrypted}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer for shift.")

# Decrypt button callback
def decrypt_text():
    try:
        shift = int(shift_entry.get())
        message = message_entry.get("1.0", tk.END).strip()
        decrypted = caesar_decrypt(message, shift)
        output_text.set(f"Decrypted Message:\n{decrypted}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer for shift.")

# GUI Setup
root = tk.Tk()
root.title("Caesar Cipher Encryption/Decryption")
root.geometry("500x400")
root.resizable(False, False)

# Input Fields
tk.Label(root, text="Enter your message:", font=('Arial', 12)).pack(pady=5)
message_entry = tk.Text(root, height=5, width=50)
message_entry.pack(pady=5)

tk.Label(root, text="Enter shift value (integer):", font=('Arial', 12)).pack(pady=5)
shift_entry = tk.Entry(root)
shift_entry.pack(pady=5)

# Buttons
tk.Button(root, text="Encrypt", command=encrypt_text, bg="lightblue", width=15).pack(pady=5)
tk.Button(root, text="Decrypt", command=decrypt_text, bg="lightgreen", width=15).pack(pady=5)

# Output
output_text = tk.StringVar()
tk.Label(root, textvariable=output_text, font=('Arial', 12), wraplength=400, justify="left").pack(pady=10)

root.mainloop()
