from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card,filp_timer
    window.after_cancel(filp_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(card_word,text=current_card["French"],fill="black")
    canvas.itemconfig(card_background,image=front_img)
    filp_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English",fill="white")
    canvas.itemconfig(card_word, text=current_card["English"],fill="white")
    canvas.itemconfig(card_background,image=back_img)


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv",index=False)
    next_card()




window = Tk()
window.title("Flash Card Game")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

filp_timer = window.after(3000,func=flip_card)

canvas = Canvas(width=800, height=526)
front_img = PhotoImage(file="./images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
card_background = canvas.create_image(400,263,image=front_img)
card_title = canvas.create_text(400,150,text="", font=("arial",40,"italic"))
card_word = canvas.create_text(400,263,text="", font=("arial",60,"bold"))
canvas.grid(row=0,column=0,columnspan=2)



right_img = PhotoImage(file="./images/right.png")
button1 = Button(image=right_img,highlightthickness=0,command=is_known)
button1.grid(row=1,column=1)

wrong_img = PhotoImage(file="./images/wrong.png")
button2 = Button(image=wrong_img,highlightthickness=0,command=next_card)
button2.grid(row=1,column=0)




next_card()

window.mainloop()

