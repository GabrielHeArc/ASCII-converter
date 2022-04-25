import shutil
from PIL import Image
import datetime
import numpy as np
from math import ceil
import os
import cv2
from datetime import datetime
from lib import *
from settings import *
import os
import datetime
from lib2to3.pytree import convert
from math import ceil
import ffmpeg
from datetime import datetime
from settings import *


Image.MAX_IMAGE_PIXELS = 10000000000000

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


def main_image(path, image_definition, gray=False):

    timestamp = datetime.now()  # fromisoformat('yyyy-MM-dd-hh:mm:ss')
    timestamp = timestamp.strftime("%m-%d-%Y-%H-%M-%S")
    if gray:
        image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    else:
        image = cv2.imread(path)

    process(image, timestamp, image_definition)
    os.remove(f"temp/ascii_image_{timestamp}.txt")
    return timestamp


def resize_array(image, image_definition):
    image_definition_x = image_definition.value[0]
    image_definition_y = image_definition.value[1]

    x = image_definition_x / image.shape[0]
    y = image_definition_y / image.shape[1]
    x = x if x <= 1 else 1
    y = y if y <= 1 else 1

    image = cv2.resize(image, None, fx=x, fy=y,
                       interpolation=cv2.INTER_AREA)
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


def process(image, timestamp, image_definition, multiple_frame=False, counter=0):
    image = resize_array(image, image_definition)

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


def main_video(file_name, image_definition):
    video_capture = cv2.VideoCapture(file_name)

    if not video_capture.isOpened():
        print("Could not open video file")
        return False
    else:
        frame_count = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))
        frame_rate = float(video_capture.get(cv2.CAP_PROP_FPS))
        timestamp = datetime.now()
        timestamp = timestamp.strftime("%m-%d-%Y-%H-%M-%S")

        convert_video(video_capture, image_definition, timestamp, frame_count)
        assemble_video(frame_rate, timestamp, image_definition)

        os.remove(f"temp/ascii_image_{timestamp}.txt")
        shutil.rmtree(f"temp/{timestamp}", ignore_errors=False, onerror=None)


def convert_video(video_capture, image_definition, timestamp, frame_count):
    success = 1
    loading = 0
    count = 0
    percent = 1 / frame_count * 100
    while success:
        if ceil(loading) != ceil(loading+percent):
            print("Loading : " + str(ceil(loading)) + "%")
        loading += percent
        success, image_array = video_capture.read()

        image_array = cv2.cvtColor(image_array, cv2.COLOR_BGR2GRAY)
        process(image_array, timestamp, image_definition,
                multiple_frame=True, counter=count)
        count += 1
        if count == frame_count-1:
            break  # work around because of unresolved error


def assemble_video(frame_rate, timestamp, image_definition):
    rescaled_frames = ffmpeg.input(
        f'temp/{timestamp}/ascii_image_%d.png', framerate=frame_rate)
    ffmpeg.output(
        rescaled_frames, f'result/video/movie_{image_definition.name}_{timestamp}.mp4', vcodec='libx264').run()
