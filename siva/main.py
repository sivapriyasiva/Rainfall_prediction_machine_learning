import tkinter as tk
from PIL import Image, ImageTk
import os

def open_current():
    os.system("python C:\\Users\\HP\\Desktop\\siva\\currend_pred.py")

def open_future():
    os.system("python C:\\Users\\HP\\Desktop\\siva\\location_based.py")

def open_top10():
    os.system("python C:\\Users\\HP\\Desktop\\siva\\top_10.py")

def validate_login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "siva" and password == "sivarmy":
        # Create the new window and destroy the login window
        login_window.destroy()
        main_window = tk.Tk()
        main_window.title("Main Menu")
        main_window.geometry("700x700")

        # Load and resize the background image
        bg_image = Image.open("./butterfly.png")
        bg_image = bg_image.resize((1500, 1000), Image.ANTIALIAS)
        bg_photo = ImageTk.PhotoImage(bg_image)

        # Set the background image
        bg_label = tk.Label(main_window, image=bg_photo)
        bg_label.image = bg_photo
        bg_label.place(x=0, y=0)

        # Add the buttons to the main window
        current_button = tk.Button(main_window, text="Current prediction", command=open_current)
        current_button.place(x=50, y=50)

        future_button = tk.Button(main_window, text="Future prediction", command=open_future)
        future_button.place(x=50, y=100)

        top10_button = tk.Button(main_window, text="Top 10 prediction", command=open_top10)
        top10_button.place(x=50, y=150)

        main_window.mainloop()

    else:
        error_label.config(text="Invalid username or password.")

def start_loading():
    loading_label.place(x=150, y=150)

def stop_loading():
    loading_label.place_forget()

# Create the login window
login_window = tk.Tk()
login_window.title("Login")
login_window.geometry("300x250")

# Load and resize the logo image
logo_image = Image.open("./logo.png")
logo_image = logo_image.resize((500, 500), Image.ANTIALIAS)
logo_photo = ImageTk.PhotoImage(logo_image)

# Set the logo image
logo_label = tk.Label(login_window, image=logo_photo)
logo_label.image = logo_photo
logo_label.pack(pady=10)

# Load the loading GIF
loading_image = Image.open("./loading.gif")
loading_photo = ImageTk.PhotoImage(loading_image)

# Create the input widgets
username_label = tk.Label(login_window, text="Username:")
username_label.pack()
username_entry = tk.Entry(login_window)
username_entry.pack()

password_label = tk.Label(login_window, text="Password:")
password_label.pack()
password_entry = tk.Entry(login_window, show="*")
password_entry.pack()

# Create the output widget
error_label = tk.Label(login_window, fg="red", text="")
error_label.pack()

# Create the button to log in
login_button = tk.Button(login_window, text="Log In", command=lambda: [start_loading(), validate_login(), stop_loading()])
login_button.pack(pady=10)

# Create the loading label
loading_label = tk.Label(login_window, image=loading_photo)

login_window.mainloop()
