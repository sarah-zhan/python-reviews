from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    chosen_letters = [random.choice(letters) for letter in range(nr_letters)]
    chosen_symbols = [random.choice(symbols) for symbol in range(nr_symbols)]
    chosen_numbers = [random.choice(numbers) for number in range(nr_numbers)]

    password_list = chosen_letters + chosen_symbols + chosen_numbers

    password = "".join(password_list)

    password_input.insert(0, password)
    # copy the passwords
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get().lower()
    email = email_input.get().lower()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if website == "" or email == "" or password == "":
        messagebox.showwarning(title="Error", message="You cannot save empty fields.")
    else:
        is_ok = messagebox.askokcancel(title="Confirmation", message=f"Are you sure you want to save it?\n"
                                                                     f"Email: {email}\n"
                                                                     f"Passwords: {password}")
        if is_ok:
            try:
                with open("data.json", mode="r") as f:
                    # read json
                    data = json.load(f)
            except FileNotFoundError:
                with open("data.json", mode="w") as f:
                    # write json
                    json.dump(new_data, f, indent=4)
            else:
                # update json
                data.update(new_data)

                with open("data.json", mode="w") as f:
                    # write json
                    json.dump(data, f, indent=4)
            finally:
                website_input.delete(0, "end")
                password_input.delete(0, "end")


# ---------------------------- SEARCH ------------------------------- #
def search_password():
    website = website_input.get().lower()
    try:
        with open("data.json", mode="r") as f:
            # read json
            data = json.load(f)
            print(data[website])
            messagebox.showinfo(title=website, message=f"Email: {data[website]['email']}\n"
                                                       f"Password: {data[website]['password']}")
    except FileNotFoundError:
        messagebox.showwarning(title="Error", message="No Data File Found.")
    except KeyError:
        messagebox.showwarning(title="Error", message="No Data Found.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

# label
website_label = Label(text="Website: ")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username: ")
email_label.grid(column=0, row=2)

password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)

# input
website_input = Entry(width=47)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

email_input = Entry(width=47)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "abc@gmail.com")
password_input = Entry(width=29)
password_input.grid(column=1, row=3)

# button
search_button = Button(text="Search", width=14, border=0, command=search_password)
search_button.grid(column=2, row=1)
password_button = Button(text="Generate Password", width=14, border=0, command=generate_password)
password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=40, height=1, highlightthickness=0, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
