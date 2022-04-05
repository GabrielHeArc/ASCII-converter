from lib2to3.pytree import convert
import time
import cv2
from cv2 import IMREAD_GRAYSCALE
from main2 import process
import png
import ffmpeg

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
        count = 0
        scale = 75
        while success:
            print(success)
            success, image_array = video_capture.read()
            image_array = cv2.cvtColor(image_array, cv2.COLOR_BGR2GRAY)
            # image_array = cv2.resize(image_array, (int(width * scale/100), int(height * scale/100)), interpolation=cv2.INTER_AREA)
            process(image_array, multiple_frame=True, counter=count)
            count += 1
            if count == frame_count-1:
                break


def assemble_video():
    print("avant")
    rescaled_frames = ffmpeg.input(
        'result/video/images/ascii_image_%d.png', framerate=25)

    print(rescaled_frames)

    print("pendant")
    rescaled_video = ffmpeg.output(
        rescaled_frames, "test.mp4").run()

    print(rescaled_video)
    print("apres")

    # ffmpeg.input('result/video/images/*.png', pattern_type='glob',
    #              framerate=25).output('result/video/final/movie.mp4').run()


if __name__ == "__main__":
    file_name = "video/video2.mp4"

    # start = time.time()
    # convert_video(file_name, "result/video/final/video")
    # inter1 = time.time()
    # print("Convert video time : ", inter1 - start)

    assemble_video()
    # inter2 = time.time()
    # print("Assemble video time : ", inter2 - inter1)

    # print("Total Time: ", inter2 - start)
