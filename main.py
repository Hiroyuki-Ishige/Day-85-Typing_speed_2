import tkinter
from tkinter import *
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
# root.minsize(width=WIDTH, height=HEIGHT)
# root.config(padx=20, pady=20)  # padding for window
root.grid_rowconfigure(0, weight=1)
root.columnconfigure(0,weight=1)

frame_main = tkinter.Frame(root, bg="gray")
frame_main.grid(sticky='news')

# Set parts -------------------------------------------------------------#
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

# Get word for typing test. This is to get from Wikipedia
text_to_type = get_wiki("Japan airlines")

# create a frame for canvas------------------------------------------------------#
frame_canvas = tkinter.Frame(frame_main)
frame_canvas.grid(row=2, column=0, pady=(5, 0), sticky='nw')
frame_canvas.grid_rowconfigure(0, weight=1)
frame_canvas.grid_columnconfigure(0, weight=1)

# Add a canvas in the frame
canvas = tkinter.Canvas(frame_canvas, bg="yellow")
canvas.grid(row=0, column=0, sticky="news")

# Link scrollbar to the Canvas
vsb=Scrollbar(frame_canvas, orient="vertical", command=canvas.yview)
vsb.grid(column=1, row=0, sticky="ns")
canvas.configure(yscrollcommand=vsb.set)

# Create a frame to contain the buttons
frame_buttons = tkinter.Frame(canvas, bg="blue")
canvas.create_window((0, 0), window=frame_buttons, anchor='nw')

#TODO add text box on Canvas
text_box = Text(root, font=("arial, 20"), height=10, width=60, )
text_box.insert(END, text_to_type)
# v.config(command=text_box.yview)
text_box.grid(column=3, row=3)






# TODO set timer and forced to stop type
# TODO count typed words
# TODO check typed words
# TODO recored score (Name, date&time, score)


# event roop
root.mainloop()