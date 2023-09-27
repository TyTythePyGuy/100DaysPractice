from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = site_entry.get()
    user = username_entry.get()
    pw = password_entry.get()
    new_data = {
        website: {
            "email": user,
            "password": pw,
        }
    }

    if len(website) == 0 or len(pw) == 0:
        messagebox.showerror(title="Oops!", message="Please do not leave any fields empty.")
    else:
        try:
            with open('data.json', 'r') as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open('data.json', 'w') as data_file:
                # saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            site_entry.delete(0, END)
            password_entry.delete(0, END)

# --------------------------SEARCH INFO ------------------------------- #
def find_password():
    website = site_entry.get()
    if len(website) == 0:
        messagebox.showerror(title="No Website", message="Please input a website before you search.")
    else:
        try:
            with open('data.json') as data_file:
                #opening data to find website combo
                pw_data = json.load(data_file)
                if website in pw_data:
                    password = pw_data[website]["password"]
                    username = pw_data[website]["email"]
                    messagebox.showinfo(title=f"{website.title()}", message=f"Username: {username}\nPassword: {password}")
                else:
                    messagebox.showerror(title="No Website", message="No details for the website exist")
        except FileNotFoundError:
            messagebox.showerror(title="No File", message="No Data File Found")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Labels
site = Label(text="Website:")
site.grid(row=1, column=0)

username = Label(text="Email/Username:")
username.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
site_entry = Entry(width=25)
site_entry.grid(row=1, column=1)
site_entry.focus()

username_entry = Entry(width=50)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(0, "youremail@gmail.com")

password_entry = Entry(width=25)
password_entry.grid(row=3, column=1)

# Buttons
gen_pass = Button(text="Generate Password", command=generate_password)
gen_pass.grid(row=3, column=2)

add = Button(text="Add", width=36, command=save)
add.grid(row=4, column=1, columnspan=2)

search = Button(text="Search", width=15, command = find_password)
search.grid(row=1, column=2)

window.mainloop()
