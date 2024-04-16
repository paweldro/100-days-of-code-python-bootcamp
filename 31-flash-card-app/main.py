from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

words_data_frame = pandas.read_csv("./data/french_words.csv")
words_dict = words_data_frame.to_dict(orient="records")

try:
    words_to_learn_data_frame = pandas.read_csv("./data/french_words_to_learn.csv")
except FileNotFoundError:
    words_to_learn_data_frame = pandas.DataFrame(words_dict)
    words_to_learn_data_frame.to_csv("./data/french_words_to_learn.csv", index=False)
except pandas.errors.EmptyDataError:
    words_to_learn_data_frame = pandas.DataFrame(words_dict)
    words_to_learn_data_frame.to_csv("./data/french_words_to_learn.csv", index=False)

words_to_learn_dict = words_to_learn_data_frame.to_dict(orient="records")

current_card = random.choice(words_dict)
print(len(words_to_learn_dict))


def flip_card_back():
    canvas.itemconfig(card_img, image=card_back_img)
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")
    canvas.itemconfig(title_text, text="English", fill="white")


def flip_card_front():
    canvas.itemconfig(card_img, image=card_front_img)
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    canvas.itemconfig(title_text, text="French", fill="black")


def new_word():
    global current_card, timer
    window.after_cancel(timer)
    if len(words_to_learn_dict) == 0:
        canvas.itemconfig(card_img, image=card_front_img)
        canvas.itemconfig(word_text, text="You know all the words. Reset the program to start over.", fill="black",
                          font=("Arial", 15, "italic"))
        canvas.itemconfig(title_text, text="Congratulations!", fill="black")
    else:
        current_card = random.choice(words_to_learn_dict)
        flip_card_front()
        timer = window.after(3000, func=flip_card_back)


def right_button_on_click():
    word_dict = {'French': current_card["French"], 'English': current_card["English"]}
    for word in words_to_learn_dict:
        if word["French"] == word_dict["French"]:
            words_to_learn_dict.remove(word)

    new_words_to_learn_data_frame = pandas.DataFrame(words_to_learn_dict)
    new_words_to_learn_data_frame.to_csv("./data/french_words_to_learn.csv", index=False)

    new_word()


def wrong_button_on_click():
    new_word()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

timer = window.after(3000, func=flip_card_back)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
card_img = canvas.create_image(400, 263, image=card_front_img)

title_text = canvas.create_text(400, 150, text="French", fill="black", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 280, text=current_card["French"], fill="black", font=("Arial", 60, "bold"))

canvas.grid(row=0, column=0, columnspan=2)

right_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=right_button_on_click)
right_button.grid(row=1, column=1)

wrong_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=wrong_button_on_click)
wrong_button.grid(row=1, column=0)

window.mainloop()
