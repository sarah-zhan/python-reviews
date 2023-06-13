from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=50)
window.config(padx=30, pady=20)

# entry
input = Entry(width=10)
input.grid(column=1, row=0)

# label
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)
miles_label.config(padx=10)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)
is_equal_label.config(padx=10)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

result_label = Label(text="0")
result_label.grid(column=1, row=1)


# button
def button_click():
    result_label["text"] = round(int(input.get()) * 1.609, 2)


button = Button(text="Calculate", command=button_click)
button.grid(column=1, row=2)

window.mainloop()
