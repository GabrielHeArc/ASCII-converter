import PIL.Image
import os
import text_to_image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from lib import *

from text_to_image import encode_file
from PIL import Image, ImageChops
from math import ceil
from PIL import (
    Image,
    ImageFont,
    ImageDraw,
)

ASCII_CHARS = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]


def resize_image(image, new_width=300):
    width, height = image.size
    new_height = new_width * height / width
    return image.resize((int(new_width), int(new_height)))


def to_greyscale(image):
    return image.convert("L")


def pixel_to_ascii(image):
    pixels = image.getdata()  # Array of pixels
    ascii_str = ""
    for pixel in pixels:
        ascii_str += ASCII_CHARS[pixel//25]
        ascii_str += ASCII_CHARS[pixel//25]
    return ascii_str


def process_array(array_image):
    # resize_image image
    array_image = resize_image(array_image)

    print(array_image)
    exit(0)

    # convert image to greyscale image
    greyscale_image = to_greyscale(image)

    # convert greyscale image to ascii characters
    ascii_str = pixel_to_ascii(greyscale_image)

    img_width = 2*greyscale_image.width  # 2 characters width = 1 pixel width
    ascii_str_len = len(ascii_str)
    ascii_img = ""

    # Split the string based on width  of the image
    for i in range(0, ascii_str_len, img_width):
        ascii_img += ascii_str[i:i+img_width] + "\n"
    # save the string to a file
    with open("text/ascii_image.txt", "w") as f:
        f.write(ascii_img)
    img = textfile_to_image("text/ascii_image.txt")

    img = trim(img)
    img.save("result/image.jpg")


def process_path(path):
    # path = "images/lena.jpg"  # input("Enter the path to the image field : \n")
    try:
        image = Image.open(path)
    except:
        print(path, "Unable to find image ")

    # resize_image image
    image = resize_image(image)

    # convert image to greyscale image
    greyscale_image = to_greyscale(image)

    # convert greyscale image to ascii characters
    ascii_str = pixel_to_ascii(greyscale_image)

    img_width = 2*greyscale_image.width  # 2 characters width = 1 pixel width
    ascii_str_len = len(ascii_str)
    ascii_img = ""

    # Split the string based on width  of the image
    for i in range(0, ascii_str_len, img_width):
        ascii_img += ascii_str[i:i+img_width] + "\n"
    # save the string to a file
    with open("text/ascii_image.txt", "w") as f:
        f.write(ascii_img)
    img = textfile_to_image("text/ascii_image.txt")

    img = trim(img)
    img.save("result/image.jpg")


if __name__ == "__main__":
    #process_path("images/lena.jpg")
    process_array(Image.open("images/lena.jpg"))
