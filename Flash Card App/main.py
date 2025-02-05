# ---------------------------- IMPORTS ---------------------------- #
from tkinter import *
import pandas
import random

# ---------------------------- CONSTANTS ---------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")


# ---------------------------- READING DATA ---------------------------- #
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except:
    data = pandas.read_csv("data/french_words.csv")
french_words = data.French.to_list()
english_words = data.English.to_list()


# ---------------------------- FLIPPING CARD ---------------------------- #
def flip_card():
    index = french_words.index(canvas.itemcget(displayed_word, "text"))
    english_translation = english_words[index]
    canvas.itemconfig(displayed_word, text=english_translation)
    canvas.itemconfig(language, text="English")
    canvas.itemconfig(card_image, image=back_pic)
    right_btn.config(state="normal")
    wrong_btn.config(state="normal")

# ---------------------------- SAVING DATA ------------------------------- #
def update_known_words():
    index = english_words.index(canvas.itemcget(displayed_word, "text"))
    with open("data/words_to_learn.csv", "w") as file:
        file.write("French,English\n")
        for i in range(len(french_words)):
            if i != index:
                file.write(f"{french_words[i]},{english_words[i]}\n")
    french_words.pop(index)
    english_words.pop(index)
    
# ---------------------------- CHANGING WORD ------------------------------- #

def switch_word():
    new_word = random.choice(french_words)
    canvas.itemconfig(displayed_word, text=new_word)
    canvas.itemconfig(card_image, image=front_pic)
    canvas.itemconfig(language, text="French")
    right_btn.config(state="disabled")
    wrong_btn.config(state="disabled")
    window.after(3000, flip_card)

def confirm_word():
    update_known_words()
    switch_word()

# ---------------------------- UI SETUP ------------------------------- #

# Window
window = Tk()
window.title("Flash Card Project")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Images
back_pic = PhotoImage(file="images/card_back.png")
front_pic = PhotoImage(file="images/card_front.png")
right_pic = PhotoImage(file="images/right.png")
wrong_pic = PhotoImage(file="images/wrong.png")


# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = canvas.create_image(400, 263, image=front_pic)
language = canvas.create_text(400, 150, text="French", font=LANGUAGE_FONT, fill="black")
displayed_word = canvas.create_text(
    400, 263, font=WORD_FONT, text=random.choice(french_words), fill="black"
)
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
right_btn = Button(
    image=right_pic, highlightthickness=0, bg=BACKGROUND_COLOR, command=confirm_word
)
wrong_btn = Button(
    image=wrong_pic, highlightthickness=0, bg=BACKGROUND_COLOR, command=switch_word
)
right_btn.grid(row=1, column=1)
wrong_btn.grid(row=1, column=0)

window.after(3000, flip_card)
window.mainloop()
