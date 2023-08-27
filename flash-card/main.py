from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


canvas = Canvas(width=800, height=526)
img_front = PhotoImage(file="./images/card_front.png")
img_back = PhotoImage(file="./images/card_back.png")
img_right = PhotoImage(file="./images/right.png")
img_wrong = PhotoImage(file="./images/wrong.png")

canvas.create_image(400, 263, image=img_front)
canvas.config(bg=BACKGROUND_COLOR)
canvas.grid(column=0, row=0)

#buttons
button_right = Button(image=img_right, highlightthickness=0)
button_right.grid(column=1, row=2)

button_wrong = Button(image=img_wrong, highlightthickness=0)
button_wrong.grid(column=0, row=2)

#label
french = Label(text="French", font=("Ariel", 40, "italic"), background="white")
french.place(x=300, y=150)
french_word = Label(text="trouve", font=("Ariel", 60, "bold"), background="white")
french_word.place(x=260, y=263)


window.mainloop()
