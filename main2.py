from PIL import Image
import datetime
import numpy as np
from PIL import (
    Image,
    ImageFont,
    ImageDraw,
)
from math import ceil
from PIL import Image, ImageChops
import PIL.Image
import os
import cv2
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from lib import *
import time


Image.MAX_IMAGE_PIXELS = 100000000000000

ASCII_CHARS = ["@", "@", "@", "@", "@", "@", "@", "@", "@", "@", "@", "@", "@", "@", "@", "@", "@", "@", "@", "@", "@", "@", "@", "@",
               "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#",
               "$", "$", "$", "$", "$", "$", "$", "$", "$", "$", "$", "$", "$", "$", "$", "$", "$", "$", "$", "$", "$", "$", "$",
               "%", "%", "%", "%", "%", "%", "%", "%", "%", "%", "%", "%", "%", "%", "%", "%", "%", "%", "%", "%", "%", "%", "%",
               "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?",
               "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*",
               "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+",
               ";", ";", ";", ";", ";", ";", ";", ";", ";", ";", ";", ";", ";", ";", ";", ";", ";", ";", ";", ";", ";", ";", ";",
               ":", ":", ":", ":", ":", ":", ":", ":", ":", ":", ":", ":", ":", ":", ":", ":", ":", ":", ":", ":", ":", ":", ":",
               ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",",
               ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."
               ]


def resize_array(image, ratio=0.25):
    # width, height = image.shape[:2]  # returns (width, height)
    # new_height = height * ratio
    # new_width = width * ratio
    image = cv2.resize(image, (0, 0), fx=ratio, fy=ratio)
    return image


def pixel_to_ascii(image):
    # pixels = image.getdata()  # Array of pixels
    ascii_chars = []
    [[ascii_chars.append(ASCII_CHARS[pixel]*2)
      for pixel in pixels] for pixels in image]
    return ''.join(ascii_chars)


def split_text(ascii_str_len, img_width, ascii_str):
    ascii_img = []
    [ascii_img.append(ascii_str[i:i+img_width] + "\n")
     for i in range(0, ascii_str_len, img_width)]
    # for i in range(0, ascii_str_len, img_width):
    #    ascii_img += ascii_str[i:i+img_width] + "\n"
    return ''.join(ascii_img)


def process(image, timestamp, multiple_frame=False, counter=0):
    # resize_image image
    # qualité image meilleure avec resize
    image = resize_array(image, 1)

    # convert greyscale image to ascii characters
    ascii_str = pixel_to_ascii(image)

    img_width = 2*image.shape[1]  # 2 characters width = 1 pixel width
    ascii_str_len = len(ascii_str)

    ascii_img = split_text(ascii_str_len, img_width, ascii_str)

    # save the string to a file
    with open(f"temp/ascii_image_{timestamp}.txt", "w+") as f:
        f.write(ascii_img)
    pathImg = f"temp/ascii_image_{timestamp}.txt"
    img = textfile_to_image(pathImg)

    img = trim(img)
    pix = np.array(img)

    if multiple_frame:
        os.makedirs(f"result/video/images/{timestamp}", exist_ok=True)
        cv2.imwrite(f"result/video/images/{timestamp}/ascii_image_" +
                    str(counter) + ".png", pix)
    else:
        cv2.imwrite(f"result/image_{timestamp}.png", pix)


def main(path, gray=False):
    if gray:
        image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    else:
        image = cv2.imread(path)
    timestamp = datetime.now()  # fromisoformat('yyyy-MM-dd-hh:mm:ss')
    timestamp = timestamp.strftime("%m-%d-%Y-%H-%M-%S")

    print(timestamp)

    #timestamp = datetime.now.strftime("%H:%M:%S")

    process(image, timestamp)


if __name__ == "__main__":
    path = "images/lena.jpg"

    # créer fichier texte temporaire avec timestamp
    # créer un dossier temporaire vide avec timestamp
    # mettre image dedans
    # détruire à la fin
    main(path, True)
