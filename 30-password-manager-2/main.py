from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
cap_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    password_entry.delete(0, 'end')
    nr_letters = random.randint(8, 10)
    nr_cap_letters = random.randint(2, 4)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    pass_list = []
    [pass_list.append(random.choice(letters)) for letter in range(0, nr_letters)]
    [pass_list.append(random.choice(cap_letters)) for cap_letter in range(0, nr_cap_letters)]
    [pass_list.append(random.choice(symbols)) for symbol in range(0, nr_symbols)]
    [pass_list.append(random.choice(numbers)) for number in range(0, nr_numbers)]

    random.shuffle(pass_list)

    pass_str = "".join(pass_list)
    password_entry.insert(0, pass_str)
    pyperclip.copy(pass_str)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    site = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        site: {
            "email": email,
            "password": password,
        }
    }
    if len(site) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")
        return 0
    is_ok = messagebox.askokcancel(title=site, message=f"These are the details entered: \nEmail: {email}"
                                                       f"\nPassword: {password} \nIs it ok to save?")
    if is_ok:

        try:
            with open("data.json", "r") as file_data:
                data = json.load(file_data)

        except FileNotFoundError:
            with open("data.json", "w") as file_data:
                json.dump(new_data, file_data, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as file_data:
                json.dump(data, file_data, indent=4)

        finally:
            website_entry.delete(0, 'end')
            password_entry.delete(0, 'end')
            website_entry.focus()

    return 0

def search_button_on_click():
    site = website_entry.get()

    try:
        with open("data.json", "r") as file_data:
            data = json.load(file_data)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if site in data:
            messagebox.showinfo(title="Search result", message=f"Email: \n{data[site]['email']} "
                                                               f"\nPassword: \n{data[site]['password']}")
        else:
            messagebox.showinfo(title="Oops", message=f"No details for {site} exists")



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(pady=20, padx=20)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0, ipadx=5)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0, ipadx=5)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0, ipadx=5)

# Entries
website_entry = Entry(width=32)
website_entry.grid(row=1, column=1, columnspan=2, sticky=W)
website_entry.focus()

email_entry = Entry(width=42)
email_entry.insert(0, "your@email.com")
email_entry.grid(row=2, column=1, columnspan=2, sticky=W)

password_entry = Entry(width=24)
password_entry.grid(row=3, column=1, sticky=W)

# Buttons
generate_button = Button(text="Generate Password", width=14, command=password_generator)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=39, command=save)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", command=search_button_on_click)
search_button.grid(row=1, column=2, sticky=E)


window.mainloop()
