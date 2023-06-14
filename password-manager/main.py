import tkinter
from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

# label
website_lable = Label(text="Website: ")
website_lable.grid(column=0, row=1)

email_label = Label(text="Email/Username: ")
email_label.grid(column=0, row=2)

password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)

# input
website_input = tkinter.Text(width=38, height=1)
website_input.grid(column=1, row=1, columnspan=2)

email_input = tkinter.Text(width=38, height=1)
email_input.grid(column=1, row=2, columnspan=2)

password_input = tkinter.Text(width=25, height=1)
password_input.grid(column=1, row=3)

# button
password_button = Button(text="Generate Password", width=14, border=0)
password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=42, height=1, highlightthickness=0)
add_button.grid(column=1, row=4, columnspan=2)



window.mainloop()