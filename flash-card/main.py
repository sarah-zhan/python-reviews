from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pd.read_csv("./data/french_words.csv")
data_dictionary_list = data.to_dict(orient='records')
# print(data_dictionary_list)

current = {}


def change_word():
    global current
    current = random.choice(data_dictionary_list)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current["French"])


# confirm learn function
def confirm_learn():
    change_word()


def review():
    change_word()


def show_english():
    global current
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current["English"], fill="white")
    canvas.itemconfig(card_background, image=img_back)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

window.after(3000, func=show_english)

canvas = Canvas(width=800, height=526)
img_front = PhotoImage(file="./images/card_front.png")
img_back = PhotoImage(file="./images/card_back.png")
img_right = PhotoImage(file="./images/right.png")
img_wrong = PhotoImage(file="./images/wrong.png")

card_background = canvas.create_image(400, 263, image=img_front)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"), tags="Title")
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"), tags="word")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

# buttons
button_right = Button(image=img_right, highlightthickness=0, command=confirm_learn)
button_right.grid(column=1, row=1)

button_wrong = Button(image=img_wrong, highlightthickness=0, command=review)
button_wrong.grid(column=0, row=1)

change_word()

window.mainloop()
