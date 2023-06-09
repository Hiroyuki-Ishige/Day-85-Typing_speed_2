import tkinter
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont

from functions import get_wiki
import difflib
import webbrowser
from datetime import date, datetime

# Difine fixed variable---------------------------
# Screen size
WIDTH = 640
HEIGHT = 400 * 2
# Set time
TIME = 10

# Set list---------------------------------------
score_list = []

# File path
score_file_path = "score_file.txt"
score_show_path = "score_show.txt"


# Function --------------------------------------
def get_sample_words():  # Get word for typing test. This is to get from Wikipedia
    global text_to_type
    word_for_sample = input_sample.get()
    text_to_type = get_wiki(word_for_sample)
    text_box.insert("1.0", text_to_type)


# count down function
# This function is pair with def countdown below.
# This is necessary to prevent starting countdown before pushing start button or
# argument error in det start_countdown()

def start_countdown():
    countdown(TIME)


def countdown(count):
    label_time.config(text=count)
    if count > 0:
        root.after(1000, countdown, count - 1)

    if count <= 0:
        textfield.config(state=DISABLED)
        count_input_word()


def count_input_word():
    global words_written
    words_written = textfield.get("1.0", tkinter.END)
    print(words_written)
    number_words_written = len(words_written)
    label_text_chara.config(text=f'Score (Total Characters Input):{number_words_written}')
    check_word(text_to_type, words_written)
    save_score(number_words_written)


# To check input word by difflib function
def check_word(text_to_type, words_written):
    diff = difflib.HtmlDiff()
    res = diff.make_file(text_to_type.split(), words_written.split(), )

    # write the res in html file
    with open('html_diff.html', 'w', encoding='utf-8') as f:
        f.write(res)

    # open html in browser
    url = "html_diff.html"
    webbrowser.open(url, new=2)


def save_score(number_words_written):
    global score_list
    name = input_name.get()
    score = (number_words_written)
    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    score_record = {"name": name, "score": score, "time_stamp": now}
    score_list.append(score_record)

    # Write score in the file
    score_file = open(score_file_path, mode="w")
    for score in score_list:
        score_file.write(str(f'Name:{score["name"]}, Score:{score["score"]}, Date&Time:{score["time_stamp"]}\n'))
    score_file.close()

    # Open score file to show score on screen
    with open(score_file_path, "r") as f:
        show_score.config(text=f'{f.read()}')

# Reset text box for input
def reset_text_box():
    textfield.config(state="normal")
    textfield.delete("1.0", tkinter.END)
    print(textfield.get("1.0", END))


# ----------------------------- UI SETUP ----------------------------------#
# Set main window --------------------------------------------------------#
root = Tk()
root.title("Typing speed challenge")
root.minsize(width=WIDTH, height=HEIGHT)
root.config(padx=20, pady=20)  # padding for window

# create frame_1 --------------------------
frame_1 = tkinter.Frame(root, )
frame_1.grid(column=0, row=0, sticky='news')

# Set canvas_1 on frame_1
canvas_1_1 = tkinter.Canvas(frame_1, )
canvas_1_1.grid(row=0, column=0, )
# -----------------------------------------

# create frame_2 --------------------------
frame_2 = tkinter.Frame(root,
                        # bg="skyblue"
                        )
frame_2.grid(column=0, row=1, sticky='news')

# Set canvases on frame_2
canvas_1_2 = tkinter.Canvas(frame_2, )
canvas_1_2.grid(row=0, column=0, )

canvas_2_2 = tkinter.Canvas(frame_2, )
canvas_2_2.grid(row=1, column=0, )

canvas_3_2 = tkinter.Canvas(frame_2, )
canvas_3_2.grid(row=2, column=0, )

# ----------------------------------------

# Set parts -----------------------------
# Input name
label_name = Label(canvas_1_1, text="Fill in your name", font=("Arial", 20))
label_name.grid(column=0, row=0)
label_name.config(padx=20, pady=20)

input_name = Entry(canvas_1_1, width=30, font=("Arial", 20))
input_name.grid(column=1, row=0)
input_name.insert(tkinter.END, "Your name")

# Input word for sample text
label_sample = Label(canvas_1_1, text="Fill in text to create sammple text", font=("Arial", 20))
label_sample.grid(column=0, row=1)
label_sample.config(padx=20, pady=20)

input_sample = Entry(canvas_1_1, width=30, font=("Arial", 20))
input_sample.grid(column=1, row=1)
input_sample.insert(tkinter.END, "fill in text")

# Buttun to get word
button_get_word = Button(canvas_1_1, text="Get word",
                         font=("Arial", 20),
                         command=get_sample_words,
                         )
button_get_word.grid(column=2, row=1)

# Show time
label_time = Label(canvas_1_1, text="Time", font=("Arial", 20))
label_time.grid(column=0, row=2)
label_time.config(padx=20, pady=20)

# Buttun to start
button_start = Button(canvas_1_1, text="Start",
                      font=("Arial", 20),
                      command=start_countdown,
                      )
button_start.grid(column=1, row=2)

# Buttun to reset text box
button_reset = Button(canvas_1_1, text="Reset",
                      font=("Arial", 20),
                      command=reset_text_box,
                      )
button_reset.grid(column=2, row=2)

# Show total length of input
label_text_chara = Label(canvas_1_1, text=f'Score (Total Characters Input)', font=("Arial", 20),
                         fg="blue")
label_text_chara.grid(column=0, row=3)
label_text_chara.config(padx=20, pady=20)

# Label "Sample text"
label_sample_text = Label(canvas_1_2, text="Sample text", font=("Arial", 20))
label_sample_text.grid(column=0, row=0)
label_sample_text.config(padx=20, pady=20)

# add text box on Canvas 1 on frame 2
text_box = Text(canvas_1_2, font=("arial", 20),
                height=5,
                # width=60,
                )
text_box.insert("1.0", "sample")
text_box.grid(column=0, row=1)

# Link scrollbar to Canvas 1 on frame 2
vsb = Scrollbar(canvas_1_2, orient="vertical", command=canvas_1_2.yview())
vsb.grid(column=1, row=1, sticky="NS")
vsb.config(command=text_box.yview)
text_box.config(yscrollcommand=vsb.set)

# Entry box to type on Canvas 2 on frame 2
label_typeinput = Label(canvas_2_2, text="Type text here", font=("Arial", 20))
label_typeinput.grid(column=0, row=0)
label_typeinput.config(padx=20, pady=20)

textfield = ScrolledText(canvas_2_2, wrap=tkinter.WORD, font=("arial", 20),
                         height=5,
                         )
textfield.grid(column=0, row=1)

# Show score on Canvas 3 on frame 2
# Label "Score"
label_score = Label(canvas_3_2, text="Score", font=("Arial", 20))
label_score.grid(column=0, row=0)
label_score.config(padx=20, pady=20)
# show score
show_score = Label(canvas_3_2, text="Score", font=("Arial", 20))
show_score.grid(column=0, row=1)

# event roop
root.mainloop()
