import os
import datetime
from lib2to3.pytree import convert
from math import ceil
import shutil
import time
import cv2
from cv2 import IMREAD_GRAYSCALE
from main2 import process
import png
import ffmpeg
from datetime import datetime


def convert_video(file_name, ratio):
    video_capture = cv2.VideoCapture(file_name)

    if not video_capture.isOpened():
        print("Could not open video file")
        return False
    else:
        width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
        frame_count = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))
        frame_rate = float(video_capture.get(cv2.CAP_PROP_FPS))

        print(width)
        print(height)
        print(frame_count)
        print(frame_rate)

        success = 1
        count = 0
        loading = 0
        percent = 1 / frame_count * 100
        timestamp = datetime.now()  # fromisoformat('yyyy-MM-dd-hh:mm:ss')
        timestamp = timestamp.strftime("%m-%d-%Y-%H-%M-%S")

        while success:
            if ceil(loading) != ceil(loading+percent):
                print("Loading : " + str(ceil(loading)) + "%")
            loading += percent
            success, image_array = video_capture.read()
            image_array = cv2.cvtColor(image_array, cv2.COLOR_BGR2GRAY)
            process(image_array, timestamp, ratio, multiple_frame=True, counter=count)
            count += 1
            if count == frame_count-1:
                break

        assemble_video(frame_rate, timestamp)
        os.remove(f"temp/ascii_image_{timestamp}.txt")




def assemble_video(frame_rate, timestamp):
    # ffmpeg.input('result/video/images/ascii_image_%d.png',
    #              framerate=frame_rate).output('result/video/final/movie.mp4').run()
    rescaled_frames = ffmpeg.input(
        f'temp/{timestamp}/ascii_image_%d.png', framerate=frame_rate)
    rescaled_video = ffmpeg.output(
        rescaled_frames, f'result/video/movie_{timestamp}.mp4', vcodec='libx264').run()


if __name__ == "__main__":
    file_name = "video/video1.mp4"
    ratio = 1
    timestamp = datetime.now()  # fromisoformat('yyyy-MM-dd-hh:mm:ss')
    timestamp = timestamp.strftime("%m-%d-%Y-%H-%M-%S")

    convert_video(file_name, ratio)
    shutil.rmtree(f"temp/{timestamp}", ignore_errors=False, onerror=None)
    os.remove(f"temp/ascii_image_{timestamp}.txt")
