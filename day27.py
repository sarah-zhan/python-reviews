from tkinter import *
import turtle

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# label
my_label = Label(text="label", font=("Arial", 24))
my_label.pack()  # need pack to show the label

# tim = turtle.Turtle()
# tim.write("testing")


# button
def button_click():
    my_label["text"] = input.get()


button = Button(text="Click Me", command=button_click)
button.pack()

# entry
input = Entry()
input.pack()

# def add(*args):
#     total = 0
#     for num in args:
#         total += num
#     return total
#
# print(add(10, 20, 50))

window.mainloop()
