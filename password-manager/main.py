from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
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

print(f"Your password is: {password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    if website_input.get() == "" or email_input.get() == "" or password_input.get() == "":
        messagebox.showwarning(title="Error", message="You cannot save empty fields.")
    else:
        is_ok = messagebox.askokcancel(title="Confirmation", message=f"Are you sure you want to save it?\n"
                                                                     f"Email: {email_input.get()}\n"
                                                                     f"Passwords: {password_input.get()}")
        if is_ok:
            with open("data.txt", mode="a") as f:
                f.write(f"{website_input.get()} | {email_input.get()} | {password_input.get()}\n")
            website_input.delete(0, "end")
            password_input.delete(0, "end")


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
password_button = Button(text="Generate Password", width=14, border=0)
password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=40, height=1, highlightthickness=0, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
