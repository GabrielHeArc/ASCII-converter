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

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from lib import *
import time

from PIL import Image
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


def resize_array(image, ratio=0.5):
    # width, height = image.shape[:2]  # returns (width, height)
    # new_height = height * ratio
    # new_width = width * ratio
    image = cv2.resize(image, (0,0), fx=ratio, fy=ratio)
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


def process(image, multiple_frame=False, counter=0):
    # resize_image image
    image = resize_array(image, 0.50) # qualité image meilleure avec resize /!\ Ne fonctionne pas si différent de 512 donc de la taille originale

    # convert greyscale image to ascii characters
    ascii_str = pixel_to_ascii(image)


    img_width = 2*image.shape[1]  # 2 characters width = 1 pixel width
    ascii_str_len = len(ascii_str)

    ascii_img = split_text(ascii_str_len, img_width, ascii_str)

    # save the string to a file
    with open("temp/ascii_image.txt", "w+") as f:
        f.write(ascii_img)
    img = textfile_to_image("temp/ascii_image.txt")

    img = trim(img)
    pix = np.array(img)

    if multiple_frame:
        cv2.imwrite("result/video/images/ascii_image_" +
                    str(counter) + ".png", pix)
    else:
        cv2.imwrite("result/image/image.png", pix)

def main(path, gray=False):
    if gray:
        image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    else:
        image = cv2.imread(path)
    process(image)


if __name__ == "__main__":
    path = "images/lena.jpg"
    main(path, True)
