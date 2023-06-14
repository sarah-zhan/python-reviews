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
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(clock_text, text="00:00")
    timer_label.config(text="Timer")
    check_label.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_sec = SHORT_BREAK_MIN * 60
    long_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_sec)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_sec)
        timer_label.config(text="Break", fg=PINK)
    elif reps % 2 != 0:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(num):
    global timer
    minute = math.floor(num / 60)
    second = num % 60
    if second < 10:
        second = f"0{second}"
    if minute < 10:
        minute = f"0{minute}"
    canvas.itemconfig(clock_text, text=f"{minute}:{second}")
    if num > 0:
        timer = window.after(100, count_down, num - 1)
    else:
        start()
        check_mark = ""
        complete = math.floor(reps / 2)
        for _ in range(complete):
            check_mark += "✔️"
        check_label.config(text=check_mark)


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
check_label = Label(font=(20), bg=YELLOW, fg=GREEN)
check_label.grid(column=1, row=3)

# button
start_button = Button(text="Start", border=0.5, command=start)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", border=0.5, command=reset)
reset_button.grid(column=2, row=2)

window.mainloop()
