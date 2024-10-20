BACKGROUND_COLOR = "#B1DDC6"

import tkinter
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
HINDI = ""
ENGLISH = ""
window_timer = None
# ----------------------------------------Timer--------------------------------------------
def timer(count):
    global window_timer
    if count > 0:
        window_timer = window.after(1000, timer, count-1)
    else:
        put_english_card()

# ----------------------------------------READ CSV----------------------------------------


french_word_df = pandas.read_csv("./data/french_words.csv")
french_word_dict = french_word_df.to_dict()
french_word_list = []
for i in range(len(french_word_df)):
    temp = [french_word_dict["French"][i], french_word_dict["English"][i]]
    french_word_list.append(temp)
random.shuffle(french_word_list)


# -------------------------------------------FUNCTIONS------------------------------------
def get_card():
    if len(french_word_list) != 0:
        to_return = french_word_list[0]
        del french_word_list[0]
        return to_return
    else:
        return None


def put_french_card():
    global HINDI, ENGLISH, window_timer
    current_word_list = get_card()
    if current_word_list is None:
        not_done_button.destroy()
        done_button.destroy()
        canvas.itemconfig(card, image=card_front_img)
        canvas.itemconfig(language, text="DONE!")
        canvas.itemconfig(word, text="Congrats :)")
        window.after_cancel(window_timer)
    else:
        FRENCH = current_word_list[0]
        ENGLISH = current_word_list[1]
        canvas.itemconfig(card, image=card_front_img)
        canvas.itemconfig(language, text="FRENCH", fill="black")
        canvas.itemconfig(word, text=FRENCH, fill="black")
        timer(1)


def put_english_card():
    canvas.itemconfig(card, image=card_back_img)
    canvas.itemconfig(language, text="ENGLISH", fill="white")
    canvas.itemconfig(word, text=ENGLISH, fill="white")


def add_to_done():
    put_french_card()


def add_to_pass():
    french_word_list.append([HINDI, ENGLISH])
    put_french_card()


# ----------------------------------------- UI SETUP --------------------------------------
window = tkinter.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_front_img = tkinter.PhotoImage(file="./images/card_front.png")
card_back_img = tkinter.PhotoImage(file="./images/card_back.png")
done_image = tkinter.PhotoImage(file="./images/right.png")
not_done_image = tkinter.PhotoImage(file="./images/wrong.png")

canvas = tkinter.Canvas(height = 526, width= 800, highlightthickness=0, bg=BACKGROUND_COLOR)
card = canvas.create_image(400, 263)
language = canvas.create_text(400, 150, font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

done_button = tkinter.Button(image=done_image, highlightthickness=0, command=add_to_done)
done_button.grid(row=1, column=1)
not_done_button = tkinter.Button(image=not_done_image, highlightthickness=0, command=add_to_pass)
not_done_button.grid(row=1, column=0)

put_french_card()

window.mainloop()