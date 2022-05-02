# importing the tkinter module and PIL that
# is pillow module
from datetime import datetime
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from settings import DefinitionVideo, DefinitionImage
from ascii_converter import main_image, main_video

from tkinter import ttk
from tkinter.ttk import *


def convert_image(path, gray):
    timestamp = datetime.now()  # fromisoformat('yyyy-MM-dd-hh:mm:ss')
    timestamp = timestamp.strftime("%m-%d-%Y-%H-%M-%S")
    name_enum = combo_image.get()
    timestamp = main_image(path, DefinitionImage[name_enum], True)

    load = Image.open(f"result/images/image_{timestamp}.png")
    original = Image.open(root.filename)
    x, y = original.size

    resized_image = load.resize((x, y))
    render = ImageTk.PhotoImage(resized_image, width=x, height=y)
    img.configure(image=render)
    img.image = render
    img.place(x=100, y=100)
    info = Label(
        tabImage, text=f"Image saved at result/images/image_{timestamp}.png")
    info.place(x=50, y=80)


def convert_video(path):
    timestamp = datetime.now()  # fromisoformat('yyyy-MM-dd-hh:mm:ss')
    timestamp = timestamp.strftime("%m-%d-%Y-%H-%M-%S")
    name_enum = combo_video.get()

    label = Label(tabVideo, text=f"Process running, please wait...")
    label.place(x=100, y=100)
    tabVideo.update()
    timestamp = main_video(path, DefinitionVideo[name_enum])
    label.destroy()
    label = Label(
        tabVideo, text=f"Video saved at result/videos/video_{timestamp}.mp4")
    label.place(x=100, y=100)


def open_file_image():
    root.filename = filedialog.askopenfilename(
        initialdir="/", title="Select file", filetypes=(("png files", "*.png"), ("all files", "*.*")))
    load = Image.open(root.filename)
    render = ImageTk.PhotoImage(load, width=700, height=700)
    img.configure(image=render)
    img.image = render
    img.place(x=100, y=100)
    img.image = render
    


def open_file_video():
    root.filename = filedialog.askopenfilename(
        initialdir="/", title="Select file", filetypes=(("mp4 files", "*.mp4"), ("all files", "*.*")))
    return root.filename


# ----------------------------------------------------------------------------------------------------------------------


# Calling the Tk (The initial constructor of tkinter)
root = Tk()
root.title("ASCII Converter")  # We will make the title of our app
root.geometry("700x700")  # Geometry of the window

# ----------------------------------------------------------------------------------------------------------------------

tabControl = ttk.Notebook(root)

# Tab image
tabImage = ttk.Frame(tabControl)
tabControl.add(tabImage, text="Convert image")
tabControl.pack(expand=1, fill="both")

# Init img label
img = Label(tabImage)

ttk.Button(tabImage, text="Exit", command=root.quit).grid(
    row=0, column=0, padx=10, pady=10)
Button(tabImage, text="Convert Image", command=lambda: convert_image(
    root.filename, False)).grid(row=0, column=2, padx=10, pady=10)
Button(tabImage, text="Open file", command=open_file_image).grid(
    row=0, column=1, padx=10, pady=10)

values_image = {}
for item in DefinitionImage:
    values_image[item.name] = item.value
list_item_image = list(values_image.keys())

Label(tabImage, text="Select image definition:").grid(
    row=1, column=0, padx=10, pady=10)
combo_image = ttk.Combobox(tabImage, values=list_item_image, state='readonly')
combo_image.grid(row=1, column=1, padx=10, pady=10)
combo_image.current(0)


# Tab Video

tabVideo = ttk.Frame(tabControl)
tabControl.add(tabVideo, text="Convert video")
tabControl.pack(expand=1, fill="both")

ttk.Button(tabVideo, text="Exit", command=root.quit).grid(
    row=0, column=0, padx=10, pady=10)
Button(tabVideo, text="Convert Video", command=lambda: convert_video(
    root.filename)).grid(row=0, column=2, padx=10, pady=10)
Button(tabVideo, text="Open file", command=open_file_video).grid(
    row=0, column=1, padx=10, pady=10)

values_video = {}
for item in DefinitionVideo:
    values_video[item.name] = item.value
list_item_video = list(values_video.keys())

Label(tabVideo, text="Select video definition:").grid(
    row=1, column=0, padx=10, pady=10)
combo_video = ttk.Combobox(tabVideo, values=list_item_video, state='readonly')
combo_video.grid(row=1, column=1, padx=10, pady=10)
combo_video.current(0)


root.mainloop()
