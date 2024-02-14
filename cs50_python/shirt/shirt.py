"""
    CS50P week 6: I/O problem set 6:CS50-P Shirt
    In a file called shirt.py, implement a program that expects exactly two command-line arguments:

        - in sys.argv[1], the name (or path) of a JPEG or PNG to read (i.e., open) as input
        - in sys.argv[2], the name (or path) of a JPEG or PNG to write (i.e., save) as output
        - The program should then overlay shirt.png (which has a transparent background) on the
          input after resizing and cropping the input to be the same size, saving the result as its output.

    Open the input with Image.open, per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open,
    resize and crop the input with ImageOps.fit, per pillow.readthedocs.io/en/stable/reference/ImageOps.html#PIL.ImageOps.fit,
    using default values for method, bleed, and centering, overlay the shirt with Image.paste,
    per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.paste,
    and save the result with Image.save, per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save.

    The program should instead exit via sys.exit:

    - if the user does not specify exactly two command-line arguments,
    - if the input's and output's names do not end in .jpg, .jpeg, or .png, case-insensitively,
    - if the input's name does not have the same extension as the output's name, or
    - if the specified input does not exist.
    - Assume that the input will be a photo of someone posing in just the right way, like these demos, so that,
      when they're resized and cropped, the shirt appears to fit perfectly.

"""

import PIL
import sys
import os

def main():
    path_in, path_out = check_args(argv)
    image_resized = prepare_image(path_in)
    shirted_image = overlay_image
    save_image(shirted_image, path_out)

def check_args(args):
    # count args
    num_args = len(args)

    # if not enough args, print msg and sys.exit
    if num_args < 3:
        sys.exit("Too few command-line arguments")

    # if too many args, print msg and sys.exit
    elif num_args > 3:
        sys.exit("Too many command-line arguments")

    # correct number of args now check if input file exists
    else:
        read_path = args[1]
        write_path = args[2]

        if not is_jpg_or_png(read_path):
            sys.exit("Not a jpg or png file")

        elif not file_exists(read_path):
            sys.exit("File does not exist")

        else:
            return read_path, write_path

def is_csv(file):
    _ , ext = os.path.splitext(file)
    return ext == ".csv"

def file_exists(file):
    return os.path.isfile(file)


