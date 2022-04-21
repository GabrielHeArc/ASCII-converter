from PIL import Image
import datetime
import numpy as np
from math import ceil
import os
import cv2
from datetime import datetime
from lib import *

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
    image = cv2.resize(image, (0, 0), fx=ratio, fy=ratio)
    return image


def pixel_to_ascii(image):
    ascii_chars = []
    [[ascii_chars.append(ASCII_CHARS[pixel]*2)
        for pixel in pixels] for pixels in image]
    return ''.join(ascii_chars)


def split_text(ascii_str_len, img_width, ascii_str):
    ascii_img = []
    [ascii_img.append(ascii_str[i:i+img_width] + "\n")
        for i in range(0, ascii_str_len, img_width)]
    return ''.join(ascii_img)


def process(image, timestamp, ratio=0.25, multiple_frame=False, counter=0):
    image = resize_array(image, ratio)

    print("XXXX")
    print(type(image))

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
        os.makedirs(f"temp/{timestamp}", exist_ok=True)
        cv2.imwrite(f"temp/{timestamp}/ascii_image_" +
                    str(counter) + ".png", pix)
    else:
        cv2.imwrite(f"result/images/image_{timestamp}.png", pix)
    print("Image enregistrée")

def main(path, timestamp, ratio, gray=False):
    if gray:
        image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    else:
        image = cv2.imread(path)

    process(image, timestamp, ratio)
    os.remove(f"temp/ascii_image_{timestamp}.txt")


if __name__ == "__main__":
    path = "images/lena.jpg"
    ratio = 1
    timestamp = datetime.now()  # fromisoformat('yyyy-MM-dd-hh:mm:ss')
    timestamp = timestamp.strftime("%m-%d-%Y-%H-%M-%S")
    # créer fichier texte temporaire avec timestamp
    # créer un dossier temporaire vide avec timestamp
    # mettre image dedans
    # détruire à la fin
    main(path, timestamp, ratio, True)