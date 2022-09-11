from tkinter import *
import pandas
import random

data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}

BACKGROUND_COLOR = "#B1DDC6"


def new_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=cardf_img)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_image, image=cardb_img)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Card Canvas

cardf_img = PhotoImage(file="images/card_front.png")
cardb_img = PhotoImage(file="images/card_back.png")

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(400, 263, image=cardf_img)
canvas.grid(column=0, row=0, columnspan=2)
card_title = canvas.create_text(400, 150, text="French", fill="black", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", fill="black", font=("Ariel", 60, "bold"))


# Buttons

right_img = PhotoImage(file="images/right.png")
right_but = Button(image=right_img, highlightthickness=0, command=new_card)
right_but.grid(column=0, row=1)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_but = Button(image=wrong_img, highlightthickness=0, command=new_card)
wrong_but.grid(column=1, row=1)

window.mainloop()
