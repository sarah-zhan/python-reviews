from tkinter import *
import turtle

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# label
my_label = Label(text="label", font=("Arial", 24))
my_label.grid(column=0, row=0)


# tim = turtle.Turtle()
# tim.write("testing")


# button
def button_click():
    my_label["text"] = input.get()


button = Button(text="Button", command=button_click)
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

# entry
input = Entry()
input.grid(column=3, row=2)

# def add(*args):
#     total = 0
#     for num in args:
#         total += num
#     return total
#
# print(add(10, 20, 50))

window.mainloop()
