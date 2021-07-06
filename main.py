from tkinter import *
from random import choice, randint
from tkinter import messagebox
import pyclip
import json
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_pass():
    global entry_website
    val_website = entry_website.get()
    global entry_username
    val_username = entry_username.get()
    global entry_password
    val_password = entry_password.get()
    new_data = {
        val_website: {
            "email": val_username,
            "password": val_password
        }
    }
    if len(entry_password.get()) > 0 and len(entry_username.get()) > 0 and len(entry_website.get()) > 0:
        is_ok = messagebox.askokcancel(title=val_website, message=f"These are the details entered: \n"
                                                                  f"Email: {val_username}\n"
                                                                  f"Password: {val_password}\nIs it ok to save?")
        if is_ok:
            try:
                with open(file="data.json", mode="r") as file:
                    data = json.load(file)
                    data.update(new_data)
                    print(data)
            except json.decoder.JSONDecodeError or FileNotFoundError:
                with open(file="data.json", mode="w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                with open(file="data.json", mode="w") as file:
                    json.dump(data, file, indent=4)
            finally:
                entry_website.delete(0, END)
                entry_password.delete(0, END)
    else:
        messagebox.showinfo("Warning!", "Please don't leave any fields blank!")
# ---------------------------- GENERATE NEW PASSWORD ------------------------------- #


def generate_pass():
    global entry_password
    nums = randint(10, 100)
    sp_chars = ""
    for num in range(4):
        sp_chars += choice(["%", "-", "#", "$", "^"])
    entry_password.delete(0, "end")
    entry_password.insert(0, f"Doudles{nums}{sp_chars}")
    pyclip.copy(f"Doudles{nums}{sp_chars}")
    print("updated")


# ---------------------------- UI SETUP ------------------------------- #

# ---------------------------- window creation ------------------------------- #
window = Tk()  # Create window as an object of class Tk()
window.title("Password Manager")  # Set the title of the window object to "Password Manager"
window.config(padx=20, pady=20)  # Set window padding to make it look fancier

# ---------------------------- VARIABLE DECLARATION ------------------------------- #
logo_img = PhotoImage(file="logo.png")  # Create the logo_img object with the png we have in the same directory

# ---------------------------- canvas creation ------------------------------- #
canvas = Canvas(height=200, width=140)  # Create the canvas object that we are going to put on the window object
canvas.create_image(70, 100, image=logo_img)  # Lay the logo_img right in the middle of the canvas

# ---------------------------- label creation ------------------------------- #
label_website = Label(text="Website:")  # Create label class object website to display the text "Website:"
label_username = Label(text="Email/Username:")  # Create label class object username to display the text "Username:"
label_password = Label(text="Password:")  # Create label class object password to display the text "Password:"

# ---------------------------- field creation ------------------------------- #
entry_website = Entry(width=32)
entry_username = Entry(width=32)
entry_password = Entry(width=22)

# ---------------------------- button creation ------------------------------- #
button_generate_password = Button(text="Generate", font=("arial", 9), height=1, width=7, anchor="w")
button_add = Button(text="Add", width=33, height=1, font=("arial", 9))  # This button is going to add the records to CSV

# ---------------------------- place the objects on the grid------------------------------- #
canvas.grid(column=1, row=0)  # Place the canvas at 1,0

label_website.grid(column=0, row=1, sticky="e")  # Place the label at 0,1
entry_website.grid(column=1, row=1, sticky="w", columnspan=2)

label_username.grid(column=0, row=2, sticky="e")  # Place the label at 0,2
entry_username.grid(column=1, row=2, sticky="w", columnspan=2)

label_password.grid(column=0, row=3, sticky="ne")  # Place the label at 0,3
entry_password.grid(column=1, row=3, sticky="nw", columnspan=1)
button_generate_password.grid(column=2, row=3, sticky="w")

button_add.grid(column=1, row=4, sticky="nw", columnspan=2)

# ---------------------------- primary features ------------------------------- #
entry_username.insert(0, "gabe@fordltc.net")
button_generate_password.config(command=generate_pass)
button_add.config(command=save_pass)

# ---------------------------- main loop ------------------------------- #
window.mainloop()
