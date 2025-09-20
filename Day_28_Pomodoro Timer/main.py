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
checkmarks = ""
count_refresh = ""
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global checkmarks
    global reps
    checkmarks = ""
    reps = 0

    label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    text.config(text="")
    window.after_cancel(count_refresh)

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps

    reps +=1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        label.config(text="Long Break", fg=RED)
        countdown(long_break_sec)
    elif reps % 2 == 0:
        label.config(text="Short Break", fg=PINK)
        countdown(short_break_sec)
    else:
        label.config(text="Work", fg=GREEN)
        countdown(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global checkmarks
    global count_refresh

    min = int(count/60)
    sec = int(60*(count/60 - int(count/60)))
    if int(60*(count/60 - int(count/60))) < 10:
        sec = f"0{sec}"
    canvas.itemconfig(timer_text, text=f"{min}:{sec}")
    if count >= 0:
        count_refresh = window.after(1000, countdown, count - 1)
    else:
        if reps%2 != 0:
            checkmarks += "✔️"
            text.config(text=checkmarks)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file=r"tomato.png")
canvas.create_image(100, 110.5, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=2, row=2)

label = Label(text="Timer")
label.config(bg=YELLOW,fg=GREEN, font=(FONT_NAME, 30, "bold"))
label.grid(column=2, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=1, row=3)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=3, row=3)

text = Label(fg=GREEN, bg=YELLOW)
text.grid(column=2, row=4)

window.mainloop()