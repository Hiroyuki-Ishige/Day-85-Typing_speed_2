import tkinter
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont

from functions import get_wiki


# count down function
def start_countdown():
    countdown(5)


def countdown(count):
    label_time.config(text=count)
    if count > 0:
        root.after(1000, countdown, count - 1)


# ----------------------------- UI SETUP ----------------------------------#
# fixed variable
WIDTH = 640
HEIGHT = 400 * 2

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
frame_2 = tkinter.Frame(root, bg="skyblue")
frame_2.grid(column=0, row=1, sticky='news')

# Set canvas_1 on frame_2
canvas_1_2 = tkinter.Canvas(frame_2, )
canvas_1_2.grid(row=0, column=0, )

# Add a canvas_2 on frame_2
canvas_2_2 = tkinter.Canvas(frame_2, )
canvas_2_2.grid(row=1, column=0, )
# ----------------------------------------

# Set parts -----------------------------
# Input name
label_name = Label(canvas_1_1, text="Fill in your name", font=("Arial", 20))
label_name.grid(column=0, row=0)
label_name.config(padx=20, pady=20)

input_name = Entry(canvas_1_1, width=30, font=("Arial", 20))
input_name.grid(column=1, row=0)
input_name.insert(tkinter.END, "Your name")

# Show time
label_time = Label(canvas_1_1, text="Time", font=("Arial", 20))
label_time.grid(column=0, row=1)
label_time.config(padx=20, pady=20)

# Buttun to start
button_start = Button(canvas_1_1, text="Start",
                      font=("Arial", 20),
                      command=start_countdown,
                      )
button_start.grid(column=1, row=1)

# Get word for typing test. This is to get from Wikipedia
text_to_type = get_wiki("Japan airlines")

# add text box on Canvas 1 on frame 2
text_box = Text(canvas_1_2, font=("arial", 20),
                height=5,
                # width=60,
                )
text_box.insert("1.0", text_to_type)
text_box.grid(column=0, row=0)

# Link scrollbar to Canvas 1 on frame 2
vsb = Scrollbar(canvas_1_2, orient="vertical", command=canvas_1_2.yview())
vsb.grid(column=1, row=0, sticky="NS")
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

# TODO set timer and forced to stop type
# TODO count typed words
# TODO check typed words
# TODO recored score (Name, date&time, score)


# event roop
root.mainloop()
