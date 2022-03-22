import math
import os
import pathlib
from sys import argv
import time
from io import BufferedReader, BufferedWriter
import cv2


def main() -> None:
    # Load the file name from the command line arguments.
    file_name = "videos/video.mp4"
    # Generate the output file name.
    output_name = "video.ascii"

    # Take the starting time to calculate the total time taken to convert the video.
    start = time.time()

    # Convert the video.
    success = convert_video(file_name, output_name)

    if success:
        print(f'\nConversion successful.\nTime: {time.time() - start}')
        print(f'\nOutput file saved as "{output_name}"')
    else:
        print('\nConversion failed')
        # If the conversion failed, delete the output file, if it was created.
        if os.path.exists(output_name):
            os.remove(output_name)


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

        print("ALL OK")
    # Create the output file.
    with open(output_name, 'wb') as output_file:
        # Write the header to the file with some useful metadata.
        write_file_header(output_file, width, height, frame_rate, frame_count) # write info in header file

    return True


def write_file_header(output_file: BufferedWriter, width: int, height: int, frame_rate: float, frame_count: int) -> None:
    """
    Writes the header of the file.
    The header takes up the first 13 bytes of the file.
    The byte order is big endian.
    """
    output_file.write(
        int.to_bytes(width, 2, 'big') +      # First 2 bytes: width
        int.to_bytes(height, 2, 'big') +     # Second 2 bytes: height
        normalize_frame_rate(frame_rate) +   # Third byte: frame rate
        int.to_bytes(frame_count, 8, 'big')  # Last 8 bytes: frame count
    )


def normalize_frame_rate(frame_rate: float) -> bytes:
    """
    Normalizes the frame rate to an unsigned byte value between 1 and 255.
    """
    frame_rate = math.ceil(frame_rate)
    if frame_rate > 255:
        frame_rate = 255
    elif frame_rate < 1:
        frame_rate = 1

    return bytes([frame_rate])


if __name__ == "__main__":
    main()
    print("end")
