# importing the tkinter module and PIL that
# is pillow module
from datetime import datetime
from tkinter import *
from tkinter import filedialog
from turtle import back, forward
from PIL import ImageTk, Image
import cv2
from numpy import can_cast
from main2 import process, main


def convert_image(path, ratio, gray):
    timestamp = datetime.now()  # fromisoformat('yyyy-MM-dd-hh:mm:ss')
    timestamp = timestamp.strftime("%m-%d-%Y-%H-%M-%S")
    print(ratio)
    main(path, timestamp, ratio, True)

    canvas= Canvas(root, width= 600, height= 400)

    load = Image.open("result/images/image_" + timestamp + ".png")
    image_resize = load.resize((300, 300), Image.ANTIALIAS)
    new_image = ImageTk.PhotoImage(image_resize)
    canvas.create_image(0, 0, image=new_image, anchor='nw')
    canvas.grid(row=6, column=0, columnspan=10, rowspan=10)
    # render = ImageTk.PhotoImage(load)
    # img = Label(root, image=render)
    # img.place(x=100, y=100)
    # List of the images so that we traverse the list
    # label = Label(image=ima)

    # We have to show the box so this below line is needed
    # img.grid(row=5, column=0, columnspan=10, rowspan=10)
    # img.image = render


def convert_video():
    pass


def open_file():
    root.filename = filedialog.askopenfilename(
        initialdir="/", title="Select file", filetypes=(("png files", "*.png"), ("all files", "*.*")))
    print(root.filename)
    # image_no_1 = ImageTk.PhotoImage(Image.open(root.filename))
    load = Image.open(root.filename)
    render = ImageTk.PhotoImage(load)
    img = Label(root, image=render)
    img.place(x=100, y=100)
    # List of the images so that we traverse the list
    # label = Label(image=ima)

    # We have to show the box so this below line is needed
    img.grid(row=2, column=0, columnspan=10, rowspan=10)
    img.image = render


# Calling the Tk (The initial constructor of tkinter)
root = Tk()
slider = Scale(root, from_=0.1, to=1, resolution=0.1, orient=HORIZONTAL)

# We will make the title of our app as Image Viewer
root.title("ASCII Converter")

# The geometry of the box which will be displayed
# on the screen
root.geometry("700x700")


# Adding the images using the pillow module which
# has a class ImageTk We can directly add the
# photos in the tkinter folder or we have to
# give a proper path for the images


# root.quit for closing the app
button_exit = Button(root, text="Exit",
                     command=root.quit)
button_convert_image = Button(
    root, text="Convert Image", command=lambda: convert_image(root.filename, slider.get(), False))
button_open_file = Button(
    root, text="Open file", command=open_file)

# grid function is for placing the buttons in the frame

button_exit.grid(row=0, column=0)
button_open_file.grid(row=0, column=1)
slider.grid(row=0, column=2)
button_convert_image.grid(row=0, column=3)


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
