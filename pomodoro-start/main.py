from tkinter import *
import math

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

def reset_timer():
    global reps
    window.after_cancel(timer)
    #timer_text 00:00
    canvas.itemconfig(time_left, text="00:00")
    #title_label "Timer"
    reps = 0
    timer_text.config(text="Timer")
    #reset check_marks
    checkmarks.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60

    # if it's the 8th rep:
    if reps % 8 == 0:
        count_down(long_break_secs)
        timer_text.config(text="Break", fg=RED)
    # if it's the 2nd/4th/6th rep:
    elif reps % 2 == 0:
        count_down(short_break_secs)
        timer_text.config(text="Break", fg=PINK)
    # if it's the 1st/3rd/5th/7th rep:
    else:
        count_down(work_secs)
        timer_text.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    for _ in range(0, 10):
        if count_sec == _:
            count_sec = f"0{_}"

    canvas.itemconfig(time_left, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += '✔'
        checkmarks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
time_left = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(row=1, column=1)

timer_text = Label(text="Timer", font=(FONT_NAME, 40, "bold"))
timer_text.config(fg=GREEN, bg=YELLOW)
timer_text.grid(row=0, column=1)

start_button = Button(text="Start", bg=PINK, highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", bg=PINK, highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

checkmarks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25, "normal"))
checkmarks.grid(row=3, column=1)

window.mainloop()
