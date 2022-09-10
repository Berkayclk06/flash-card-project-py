from tkinter import *
import pandas
import random

data = pandas.read_csv("data/french_words.csv")
french_dict = {row.French: row.English for (index, row) in data.iterrows()}

BACKGROUND_COLOR = "#B1DDC6"

b = random.choice(list(french_dict))

def new_card():
    global word_text
    a = random.choice(list(french_dict))
    canvas_f.itemconfig(word_text, text=a)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Card Canvas

cardf_img = PhotoImage(file="images/card_front.png")
cardb_img = PhotoImage(file="images/card_back.png")

canvas_f = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_f.create_image(400, 263, image=cardf_img)
canvas_f.grid(column=0, row=0, columnspan=2)
lang_text = canvas_f.create_text(400, 150, text="French", fill="black", font=("Ariel", 40, "italic"))
word_text = canvas_f.create_text(400, 263, text=b, fill="black", font=("Ariel", 60, "bold"))

# Buttons

right_img = PhotoImage(file="images/right.png")
right_but = Button(image=right_img, highlightthickness=0, command=new_card)
right_but.grid(column=0, row=1)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_but = Button(image=wrong_img, highlightthickness=0, command=new_card)
wrong_but.grid(column=1, row=1)

window.mainloop()
