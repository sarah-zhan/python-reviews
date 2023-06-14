import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start():
    count_down(8*60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(num):
    minute = math.floor(num / 60)
    second = num % 60
    if second < 10:
        second = f"0{second}"
    if minute < 10:
        minute = f"0{minute}"
    canvas.itemconfig(clock_text, text=f"{minute}:{second}")
    if num > 0:
        window.after(1000, count_down, num - 1)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=40, bg=YELLOW)



canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
clock_text = canvas.create_text(100, 132, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(column=1, row=1)


# label
timer_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
timer_label.grid(column=1, row=0)
check_label = Label(text="✔️", font=(20), bg=YELLOW, fg=GREEN, padx=30)
check_label.grid(column=1, row=3)

# button
start_button = Button(text="Start", border=0.5, command=start)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", border=0.5)
reset_button.grid(column=2, row=2)



window.mainloop()