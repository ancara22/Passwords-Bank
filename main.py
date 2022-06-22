# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from generator import generate
from tkinter import messagebox
from tkinter import *
import json


def generate_password():
    password_entry.delete(0, END)
    password_entry.insert(0, f"{generate()}")


def search():
    website = website_entry.get()
    user = user_entry.get()

    try:
        with open(file="database.json", mode="r") as data_file:
            data = json.load(data_file)
            email = "email"
            passw = "password"

            try:
                info = data[website]
                messagebox.showinfo("Message", f"Website: {website} "
                                               f"\nUsername: {info[email]} "
                                               f"\nPassword: {info[passw]}")

            except KeyError:
                messagebox.showinfo("Message", "Data not found!")

    except FileNotFoundError:
        messagebox.showinfo("Message", "No Datas yet")



# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    user = user_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email": user,
            "password": password
        }
    }

    if website == "" or user == "" or password == "":
        messagebox.showinfo("Alert", "Empty Boxes.\nPlease, fill all the entries.")
    else:
        messagebox.showinfo("Message", "Password Added!\n\nThank you.")

        try:
            with open(file="database.json", mode="r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open(file="database.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            data.update(new_data)

            with open(file="database.json", mode="w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password saver")
window.config(padx=40, pady=60, bg="white")

logo = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
canvas.create_image(60, 100, image=logo)
canvas.grid(column=1, row=0, pady=20)

website_label = Label(text="Website", bg="white", fg="black") \
    .grid(column=0, row=1, sticky="w")
user_label = Label(text="Email/Username", bg="white", fg="black") \
    .grid(column=0, row=2, sticky="w")
password_label = Label(text="Password", bg="white", fg="black") \
    .grid(column=0, row=3, sticky="w")

website_entry = Entry(width=25, bg="white", highlightbackground="white", fg="black")
website_entry.grid(column=1, row=1, padx=30, pady=2, sticky="w")
website_entry.focus()
user_entry = Entry(width=40, bg="white", highlightbackground="white", fg="black")
user_entry.grid(column=1, row=2, padx=30, pady=2)
user_entry.insert(0, "denis10.ru@mail.ru")
password_entry = Entry(width=25, bg="white", highlightbackground="white", fg="black")
password_entry.grid(column=1, row=3, padx=30, pady=2, sticky="w")

search_btn = Button(window, text="Search", highlightthickness=0, highlightbackground='white', width=10, command=search)
search_btn.grid(column=1, row=1, sticky="e",  padx=30)

generate_btn = Button(window, text="Generate", highlightthickness=0, highlightbackground='white', width=10, command=generate_password)
generate_btn.grid(column=1, row=3, sticky="e", padx=30)
add_btn = Button(window, text="Add", highlightthickness=0, highlightbackground='white', width=37, command=save)
add_btn.grid(column=1, row=4, pady=20)

window.mainloop()
