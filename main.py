import tkinter as tk
import os

# Create the main window
window = tk.Tk()
window.title("Login")
window.configure(bg="#000000")
# Create the labels for the username and password
tk.Label(window, text="Username", font=("Arial", 20), fg="#FFFFFF", bg="#000000").grid(row=0)
tk.Label(window, text="Password", font=("Arial", 20), fg="#FFFFFF", bg="#000000").grid(row=1)

# Create the entry fields for the username and password
username_entry = tk.Entry(window, font=("Arial", 20), fg="#FFFFFF", bg="#333333", insertbackground="#FFFFFF")
password_entry = tk.Entry(window, show="*", font=("Arial", 20), fg="#FFFFFF", bg="#333333", insertbackground="#FFFFFF")


# Place the entry fields in the grid
username_entry.grid(row=0, column=1)
password_entry.grid(row=1, column=1)

# Create a counter to track the number of invalid login attempts
invalid_attempts = 0

def login():
    # Get the entered username and password
    username = username_entry.get()
    password = password_entry.get()

    # Check if the username and password are correct
    if username == "Luca" and password == "Morache1.":
        # Close the login window
        window.destroy()

        # Open a new window
        new_window = tk.Tk()
        new_window.title("OS")
        new_window.attributes("-fullscreen", True)

        # Add a close and minimize button to the top-right corner of the window
        close_button = tk.Button(new_window, text="X", font=("Arial", 20), command=new_window.destroy)
        fullscreen_button = tk.Button(new_window, text="❒", font=("Arial", 20), command=new_window.iconify)
        minimize_button = tk.Button(new_window, text="_", font=("Arial", 20), command=new_window.iconify)
        close_button.pack(side="right", anchor="ne")
        fullscreen_button.pack(side="right", anchor="ne")
        minimize_button.pack(side="right", anchor="ne")

        tk.Label(new_window, text="Welcome to the OS app!").pack()
    else:
        # Increment the counter for invalid attempts
        global invalid_attempts
        invalid_attempts += 1

        # Calculate the number of remaining attempts
        remaining_attempts = 5 - invalid_attempts

        # Check if the user has exceeded the maximum number of invalid attempts
        if invalid_attempts >= 5:
            # Close the login window
            window.destroy()
        else:
            # Display a message saying that the login is invalid and showing the number of remaining attempts
            tk.Label(window, text=f"Invalid username or password! You have {remaining_attempts} attempts remaining.").grid(row=3, column=1)

# Create the login button
tk.Button(window, text="Login", command=login).grid(row=2, column=1, sticky=tk.E)

window.mainloop()
