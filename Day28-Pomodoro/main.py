from tkinter import *
from math import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.05
LONG_BREAK_MIN = 0.2
CHECK_MARK = "✔"
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #

def reset():
    global timer
    global reps
    reps = 0
    window.after_cancel(timer)
    checks.config(text="")
    top_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    global check
    if reps <= 8:
        if reps % 8 == 0:
            count = int(LONG_BREAK_MIN*60)
            top_label.config(text="Break", fg=GREEN)
            # check += CHECK_MARK
            # checks.config(text=check)
        elif reps % 2 == 0:
            count = int(SHORT_BREAK_MIN*60)
            top_label.config(text="Break", fg=PINK)
            # check += CHECK_MARK
            # checks.config(text=check)
        else:
            count = int(WORK_MIN*60)
            top_label.config(text="Work", fg=RED)

        count_down(count)
    else:
        reset()


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global timer
    minutes = floor(count/60)
    seconds = count % 60
    if seconds <= 9:
        seconds = f"0{seconds}"
    if count >= 0:
        canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
        timer = window.after(200, count_down, count-1)
    else:
        start_timer()
        check = ""
        for _ in range(floor(reps/2)):
            check += CHECK_MARK
        checks.config(text=check)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", font=("Courier", 35, "bold"), fill="white")
canvas.grid(column=1, row=1)


top_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
top_label.grid(column=1, row=0)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset)
reset_button.grid(column=2, row=2)

checks = Label(text="", fg=GREEN, bg=YELLOW)
checks.grid(column=1, row=3)


window.mainloop()