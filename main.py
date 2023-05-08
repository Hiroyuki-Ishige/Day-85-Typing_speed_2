import tkinter
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont


# count down function
def start_countdown():
    countdown(5)

def countdown(count):
    label_time.config(text=count)
    if count > 0:
        window.after(1000, countdown, count - 1)


# ----------------------------- UI SETUP ----------------------------------#
# fixed variable
WIDTH = 640
HEIGHT = 400 * 2

# Set main window
window = Tk()
window.title("Typing speed challenge")
window.minsize(width=WIDTH, height=HEIGHT)
window.config(padx=20, pady=20)  # padding for window

# Input name
label_name = Label(text="Fill in your name", font=("Arial", 10))
label_name.grid(column=0, row=0)
label_name.config(padx=20, pady=20)

input_name = Entry(width=20)
input_name.grid(column=1, row=0)
input_name.insert(tkinter.END, "Your name")

#Show time
label_time = Label(text="Time", font=("Arial", 30))
label_time.grid(column=0, row=1)
label_time.config(padx=20, pady=20)

# Buttun to start
button_start = Button(text="Start",
                      font=("Arial", 20),
                      command=start_countdown,
                      )
button_start.grid(column=1, row=1)

# Show text to type
label_title = Label(text="Text you will type", font=("Arial", 10))
label_title.grid(column=0, row=2)
# my_label.config(text="Label") #When you would like to change label title


# TODO get word to type (from web or local file)
# TODO set timer and forced to stop type
# TODO count typed words
# TODO check typed words
# TODO recored score (Name, date&time, score)


# event roop
window.mainloop()