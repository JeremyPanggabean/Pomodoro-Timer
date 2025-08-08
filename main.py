import tkinter
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
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    checkmark_label.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 != 0:
        # if its 1st/3rd/5th/7th rep:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)
    else:
        # if its 2nd/4th/6th rep:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
            checkmark_label.config(text= marks)

# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.minsize(width=400, height=400)
window.config(background=YELLOW)
window.title("Pomodoro Timer")


canvas = tkinter.Canvas(width=220, height=330, highlightthickness=0)
canvas.config(background=YELLOW)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(112, 210, image=tomato_img)
timer_text = canvas.create_text(122, 236,text="00:00", font=(FONT_NAME, 27, "bold"), fill="white")
canvas.pack()


start_button = tkinter.Button(text="Start", fg="black", font=(FONT_NAME, 10, "bold"), highlightthickness=0, command=start_timer)
start_button.place(x=60, y=300)

reset_button = tkinter.Button(text="Reset", fg="black", font=(FONT_NAME, 10, "bold"), highlightthickness=0, command=reset_timer)
reset_button.place(x=290, y=300)

checkmark_label = tkinter.Label(fg=GREEN, bg=YELLOW)
checkmark_label.place(x=175, y=332)

title_label = tkinter.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
title_label.place(x=144, y=45)


window.mainloop()