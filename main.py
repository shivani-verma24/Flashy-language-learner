from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv("data/words_to_learn.csv")

except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    data_list = original_data.to_dict(orient="records")

else:
    data_list = data.to_dict(orient = "records")


word_info = {}

def next_card():
    global word_info, flip_Timer
    window.after_cancel(flip_Timer)

    word_info = random.choice(data_list)
    french_word = word_info["French"]
    canvas.itemconfig(card_title, text = "French", fill = "black")
    canvas.itemconfig(card_word, text = french_word, fill = "black")
    canvas.itemconfig(canvas_img, image= front_img)

    flip_Timer = window.after(3000, func= flip_card)


def flip_card():
    english_word = word_info["English"]
    canvas.itemconfig(card_title, text="English", fill = "white")
    canvas.itemconfig(card_word, text=english_word, fill = "white")
    canvas.itemconfig(canvas_img, image = back_img)

def known_word():
    data_list.remove(word_info)
    new_data = pandas.DataFrame(data_list)
    new_data.to_csv("data/words_to_learn.csv", index = False)

    next_card()


window = Tk()
window.title("Flashy Language Learner")
window.config(padx= 50, pady = 50, bg = BACKGROUND_COLOR)

flip_Timer = window.after(3000, func= flip_card)

canvas = Canvas(width = 800, height = 526)
canvas.config(bg = BACKGROUND_COLOR, highlightthickness = 0)

front_img = PhotoImage(file = "images/card_front.png")
back_img = PhotoImage(file = "images/card_back.png")
canvas_img = canvas.create_image(400, 263, image = front_img)

card_title = canvas.create_text(400, 150 ,text = "", font = ("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text = "", font = ("Arial", 60, "bold"))
canvas.grid(row = 0, column = 0, columnspan = 2)


wrong_img = PhotoImage(file = "images/wrong.png")
wrong_button = Button(image = wrong_img, highlightthickness= 0, command = next_card)
wrong_button.grid(row = 1, column = 0)

right_img = PhotoImage(file = "images/right.png")
right_button = Button(image = right_img, highlightthickness= 0, command = known_word)
right_button.grid(row = 1, column = 1)


next_card()


window.mainloop()


# Application by Shivani Verma