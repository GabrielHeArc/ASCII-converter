# importing the tkinter module and PIL that
# is pillow module
from datetime import datetime
from tkinter import *
from tkinter import filedialog
from turtle import back, forward
from PIL import ImageTk, Image
import cv2
from matplotlib import image
from numpy import can_cast
from settings import DefinitionVideo, DefinitionImage
from ascii_converter import main_image

from tkinter import ttk
from tkinter.ttk import *


def convert_image(path, image_definition, gray):
    timestamp = datetime.now()  # fromisoformat('yyyy-MM-dd-hh:mm:ss')
    timestamp = timestamp.strftime("%m-%d-%Y-%H-%M-%S")
    timestamp = main_image(path, image_definition, True)


    load = Image.open(f"result/images/image_{timestamp}.png")
    original = Image.open(root.filename)
    x, y = original.size

    resized_image = load.resize((x, y))
    render = ImageTk.PhotoImage(resized_image, width=x, height=y)
    img = Label(tabImage, image=render)
    # img.place(root, x=100, y=100)
    # # We have to show the box so this below line is needed
    # img.grid(row=2, column=0, columnspan=10, rowspan=10)
    img.place(x=100, y=100)
    img.image = render
    info = Label(tabImage, text=f"Image saved at result/images/image_{timestamp}.png")
    info.place(x=50, y=50)



    # window = open_new_window()
    # canvas = Canvas(window, width=700, height=700)
    # canvas.pack()
    # img = PhotoImage(file=f"result/images/image_{timestamp}.png")
    # img = cv2.resize(image, None, fx=0.25, fy=0.25, interpolation=cv2.INTER_AREA)
    # canvas.create_image(20, 20, anchor=NW, image=img)
    # window.mainloop()


def open_new_window():
    newWindow = Toplevel(root)
    newWindow.title("Ascii Image")
    newWindow.geometry("800x800")
    return newWindow


def open_file():
    root.filename = filedialog.askopenfilename(
        initialdir="/", title="Select file", filetypes=(("png files", "*.png"), ("all files", "*.*")))
    print(root.filename)
    load = Image.open(root.filename)
    print(load.size)
    render = ImageTk.PhotoImage(load, width=700, height=700)
    img = Label(tabImage, image=render)
    img.place(x=100, y=100)
    # We have to show the box so this below line is needed
    # img.grid(row=2, column=0, columnspan=10, rowspan=10)
    img.image = render

# ----------------------------------------------------------------------------------------------------------------------


# Calling the Tk (The initial constructor of tkinter)
root = Tk()
root.title("ASCII Converter")  # We will make the title of our app
root.geometry("700x700")  # Geometry of the window
root.filename = "images/lena.png"  # TODO TOREMOVE
tabControl = ttk.Notebook(root)
tabImage = ttk.Frame(tabControl)
tabControl.add(tabImage, text="Convert image")
tabControl.pack(expand=1, fill="both")

tabVideo = ttk.Frame(tabControl)
tabControl.add(tabVideo, text="Convert video")
tabControl.pack(expand=1, fill="both")

button_exit = ttk.Button(tabImage,
                     text="Exit",
                     command=root.quit).grid(row=0, column=0, padx=10, pady=10)
button_convert_image = Button(tabImage, text="Convert Image", command=lambda: convert_image(
    root.filename, DefinitionImage.HD, False)).grid(row=0, column=2, padx=10, pady=10)
button_open_file = Button(tabImage, text="Open file", command=open_file).grid(row=0, column=1, padx=10, pady=10)

root.mainloop()


# from tkinter import *
# from tkinter import ttk

# def calculate(*args):
#     try:
#         value = float(feet.get())
#         meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
#     except ValueError:
#         pass

# root = Tk()
# root.title("Feet to Meters")

# mainframe = ttk.Frame(root, padding="3 3 12 12")
# mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)

# feet = StringVar()
# feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
# feet_entry.grid(column=2, row=1, sticky=(W, E))

# meters = StringVar()
# ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

# ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

# ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
# ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
# ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

# for child in mainframe.winfo_children():
#     child.grid_configure(padx=5, pady=5)

# feet_entry.focus()
# root.bind("<Return>", calculate)

# root.mainloop()
