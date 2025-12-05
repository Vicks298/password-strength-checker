import tkinter as tk
from tkinter import messagebox
from password_utils import check_password_strength, hash_password

# Function to check password and display results
def check_password():
    password = password_entry.get()
    level, suggestions = check_password_strength(password)
    hashed = hash_password(password)

    # Prepare the message
    msg = f"Strength: {level}\n\n"
    if suggestions:
        msg += "Suggestions:\n"
        for s in suggestions:
            msg += "- " + s + "\n"
    msg += f"\nSHA-256 Hash:\n{hashed}"

    # Show results in a message box
    messagebox.showinfo("Password Strength Checker", msg)

# Create the main window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x200")
root.resizable(False, False)

# Label and entry
tk.Label(root, text="Enter a password:", font=("Arial", 12)).pack(pady=10)
password_entry = tk.Entry(root, show="*", width=30)
password_entry.pack()

# Button to check password
tk.Button(root, text="Check Password", command=check_password, font=("Arial", 12)).pack(pady=20)

# Run the GUI
root.mainloop()
