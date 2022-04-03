from lib2to3.pytree import convert
import time
import cv2
from cv2 import IMREAD_GRAYSCALE
from main2 import process
import png

def FrameCapture(path):

    # Path to video file
    vidObj = cv2.VideoCapture(path)

    # Used as counter variable
    count = 0

    # checks whether frames were extracted
    success = 1

    while success:

        # vidObj object calls read
        # function extract frames
        success, image = vidObj.read()

        # Saves the frames with frame-count
        cv2.imwrite("temp/frame%d.jpg" % count, image)

        count += 1

def convert_video(file_name, output_name):
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

        while success:
            success, image_array = video_capture.read(IMREAD_GRAYSCALE)
            print(image_array.shape)
            process(image_array)








if __name__ == "__main__":
    file_name = "video/video.mp4"
    start = time.time()
    convert_video(file_name, "result/video/final/video")
    end = time.time()

    print("Time: ", end - start)




