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
def reset_button_on_click():
    start_button.config(state="normal")

    global reps
    reps = 0
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    checkmark_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_button_on_click():
    start_button.config(state="disabled")

    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        countdown(work_sec)
        timer_label.config(text="Work", fg=GREEN)

    elif reps == 2 or reps == 4 or reps == 6:
        countdown(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    elif reps == 8:
        countdown(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    else:
        reset_button_on_click()

    if reps % 2 == 0:
        checkmark_label.config(text="✓" * (reps // 2))


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global timer
    minutes = count // 60
    seconds = count % 60

    if minutes < 10:
        minutes = "0" + str(minutes)
    else:
        minutes = str(minutes)

    if seconds < 10:
        seconds = "0" + str(seconds)
    else:
        seconds = str(seconds)

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        timer = window.after(10, countdown, count - 1)
    else:
        start_button_on_click()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=204, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=tomato_img)
timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(row=1, column=1)

timer_label = Label(text="Timer", font=(FONT_NAME, 45), anchor="center")
timer_label.grid(row=0, column=1)
timer_label.config(bg=YELLOW, fg=GREEN)

start_button = Button(text="Start", font=(FONT_NAME, 15), command=start_button_on_click)
start_button.grid(row=2, column=0)
start_button.config(padx=4, pady=4, bg=GREEN, fg=RED, highlightthickness=0)

reset_button = Button(text="Reset", font=(FONT_NAME, 15), command=reset_button_on_click)
reset_button.grid(row=2, column=2)
reset_button.config(padx=4, pady=4, bg=GREEN, fg=RED, highlightthickness=0)

checkmark_label = Label(font=(FONT_NAME, 45))
checkmark_label.grid(row=3, column=1)
checkmark_label.config(padx=10, pady=10, bg=YELLOW, fg=GREEN, highlightthickness=0)

window.mainloop()
