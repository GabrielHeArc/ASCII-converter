import PIL.Image
import os
import cv2

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from lib import *
import time

from PIL import Image, ImageChops
from math import ceil
from PIL import (
    Image,
    ImageFont,
    ImageDraw,
)
import numpy as np

ASCII_CHARS = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]


def resize_array(image, new_width=300):
    # print(image.shape)
    width, height = image.shape[:2]  # shape[:2] returns (width, height)
    new_height = new_width * height / width
    image = np.resize(image, (int(new_width), int(new_height)))
    # print(image.shape)
    return image


def pixel_to_ascii(image):
    # print(image)
    # pixels = image.getdata()  # Array of pixels
    ascii_chars = []
    print(image.shape)
    # start = time.time()
    # end = time.time()
    [[ascii_chars.append(ASCII_CHARS[pixel//25]*2) for pixel in pixels] for pixels in image]
    # for pixels in image:
    #     for pixel in pixels:
    #         start = time.time()
    #         ascii_chars.append(ASCII_CHARS[pixel//25]*2)
    #         end = time.time()
    #         # print("Pixel to ascii : ", end - start)
    return ''.join(ascii_chars)


def process(image, multiple_frame=False, counter=0):
    # print(type(image))
    # resize_image image
    # image = resize_array(image, 512) # qualité image meilleure avec resize /!\ Ne fonctionne pas si différent de 512 donc de la taille originale

    # convert greyscale image to ascii characters
    print("START")
    start = time.time()
    ascii_str = pixel_to_ascii(image)
    inter = time.time()
    print("Pixel to ascii : ", inter - start)

    img_width = 2*image.shape[1]  # 2 characters width = 1 pixel width
    ascii_str_len = len(ascii_str)
    ascii_img = ""

    # Split the string based on width  of the image
    inter2 = time.time()
    for i in range(0, ascii_str_len, img_width):
        ascii_img += ascii_str[i:i+img_width] + "\n"
    # save the string to a file
    with open("text/ascii_image.txt", "w") as f:
        f.write(ascii_img)
    img = textfile_to_image("text/ascii_image.txt")
    inter3 = time.time()
    print("convert to image Time: ", inter3 - inter2)

    inter4 = time.time()
    img = trim(img)
    if multiple_frame:
        img.save("result/video/images/ascii_image_" + str(counter) + ".png")
    else:
        img.save("result/image/image.png")

    final = time.time()
    print("Save image time : ", final - inter4)
    print("Total Time: ", final - start)
    print("END")

def main(path, gray=False):
    path = "images/lena.jpg"  # Enter the path to the image field

    if gray:
        image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    else:
        image = cv2.imread(path)
    process(image)

if __name__ == "__main__":
    path = "images/lena.jpg"
    main(path, True)
