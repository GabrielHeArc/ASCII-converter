# Imports
import sys
import PIL.Image
import os
import cv2
from tkinter import *

root = Tk()

# setting font to small so the video fits into the screen
root.option_add('*Font', 'Times 1')
text = Text(root)
text.pack(expand='true', fill=BOTH)
detail = 83


def update_detail(event):  # changes video detail
    global detail
    detail = w.get()
    print(detail)


w = Scale(root, from_=30, to=200, orient=HORIZONTAL,
          command=update_detail)  # create slider to change detail
w.pack()


def generate_from_video():
    # get image and read it
    video_path = "videos/video.mp4"  # add path to your mp4 file here
    cap = cv2.VideoCapture(video_path)

    if cap.isOpened():
        framerate = cap.get(cv2.CAP_PROP_FPS)
        framecount = 0
        while(True):
            # capture frame-by-frame
            success, image = cap.read()
            img = PIL.Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY))

            # resize the image
            width, height = img.size
            aspect_ratio = height/width
            new_width = width
            new_height = aspect_ratio * new_width * 0.55
            img = img.resize((new_width, int(new_height)))

            # convert image to greyscale format
            img = img.convert('L')
            pixels = img.getdata()

            # convert to ASCII
            # values taken from https://pythoncircle.com
            chars = ["B", "S", "#", "&", "@", "$", "%", "*", "!", ":", "."]
            new_pixels = [chars[pixel//detail] for pixel in pixels]
            new_pixels = ''.join(new_pixels)

            new_pixels_count = len(new_pixels)
            ascii_image = [new_pixels[index:index + new_width]
                           for index in range(0, new_pixels_count, new_width)]
            ascii_image = "\n".join(ascii_image)

            #show in Tkinter
            text.delete('1.0', END)
            text.insert(1.0, ascii_image)
            text.update()
    else:
        print("Video not Opened!")


if __name__ == "__main__":
    generate_from_video()
    root.mainloop()
