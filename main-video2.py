
from turtle import width
import cv2
import os
import pathlib
import math
import time
from sys import argv
from io import BufferedReader, BufferedWriter


def main() -> None:
    # Get the file name from the command line arguments.
    input_file = argv[1]

    # Open the ASCII art file.
    with open(input_file, 'rb') as file:
        # Read the header to extract the metadata.
        file_info = read_header(file)

    # Load the file name from the command line arguments.
    file_name = pathlib.Path(argv[1])

    # Generate the output file name.
    output_name = pathlib.Path('result/' + file_name.stem + '.ascii')

    print("\n-- output : --")
    print(output_name)

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
        if os.path.exists(output_name.name):
            os.remove(output_name.name)


def convert_video(file_name: pathlib.Path, output_name: pathlib.Path) -> bool:
    print("\n-- file_name : --")
    print(file_name)
    print("\n-- file_name.name : --")
    print(file_name.name + '\n')

    # Open the video file.
    cap = cv2.VideoCapture(file_name.name)

    # Check if the video file was opened successfully.
    if not cap.isOpened():
        print('Could not open video file')
        return False

    # Get the video file info.
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_rate = float(cap.get(5))

    with open(output_name.name, 'wb') as output_file:
        # Write the header to the file with some useful metadata.
        write_file_header(output_file, width, height, frame_rate, frame_count)


def write_file_header(output_file: BufferedWriter, width: int, height: int, frame_rate: float, frame_count: int) -> None:
    """"
    Writes the header of the file.
    The header takes up the first 13 bytes of the file.
    The byte order is big endian.
    """
    output_file.write(
        int.to_bytes(width, 2, 'big') +     # First 2 bytes: width
        int.to_bytes(height, 2, 'big') +    # Second 2 bytes: height
        normalize_frame_rate(frame_rate) +  # Third byte: frame rate
        int.to_bytes(frame_count, 8, 'big')  # Last 8 bytes: frame count
    )


'''
  # Convert every frame of the video to ASCII art.
  counter = 0

   while cap.isOpened():
        # Read the next frame.
        ret, frame = cap.read()
        if not ret:
            break

        counter += 1
        print(f'\r{counter}/{frame_count} frames converted', end='')

        # Convert the frame to ASCII art and write it to the file.
        output_file.write(fast_convert_frame(
            bytes(frame), width, height).encode('ascii'))

    cap.release()
'''


class FileInfo:
    """A class that holds metadata about the file."""

    def __init__(self, width: int, height: int, frame_rate: int, frame_count: int):
        self.width = width
        self.height = height
        self.frame_rate = frame_rate
        self.frame_count = frame_count
        self.frame_buffer_size = (self.width * 2) * self.height

    def __str__(self):
        return f'FileInfo: {self.width}x{self.height} | {self.frame_rate} fps | {self.frame_count} frames | {self.frame_buffer_size} bytes'

    def __repr__(self) -> str:
        return self.__str__()


def read_header(file: BufferedReader) -> FileInfo:
    """Reads the header of the file and returns it in a friendly format."""
    # First 2 bytes: width
    width = int.from_bytes(file.read(2), 'big')

    # Second 2 bytes: height
    height = int.from_bytes(file.read(2), 'big')

    # Third byte: frame rate
    frame_rate = int.from_bytes(file.read(1), 'big')

    # Last 8 bytes: frame count
    frame_count = int.from_bytes(file.read(8), 'big')

    return FileInfo(width, height, frame_rate, frame_count)


def normalize_frame_rate(frame_rate: float) -> bytes:
    """ Normalizes the frame rate to an unsigned byte value between 1 and 255. """
    frame_rate = math.ceil(frame_rate)
    if frame_rate > 255:
        frame_rate = 255
    elif frame_rate < 1:
        frame_rate = 1

    return bytes([frame_rate])


if __name__ == "__main__":
    main()
    print("end")
