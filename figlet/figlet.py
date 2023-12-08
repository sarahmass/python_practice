"""
    CS50p week 4 problem set 4:
    In a file called figlet.py, implement a program that: Frank, Ian, and Glen's letters

        Expects zero or two command-line arguments:
            - Zero if the user would like to output text in a random font.
            - Two if the user would like to output text in a specific font,
              in which case the first of the two should be -f or --font, and
              the second of the two should be the name of the font.
            - Prompts the user for a str of text.
            - Outputs that text in the desired font.

        If the user provides two command-line arguments and the first is not -f or --font
        or the second is not the name of a font, the program should exit via sys.exit with
        an error message.
"""
import sys
import random
from pyfiglet import Figlet

def main():
    figlet = Figlet()

    # pass all available fonts to get_font()
    font_type = get_font(figlet.getFonts())

    # set to user defined font type or random as
    # defined by get_font()
    figlet.setFont(font=font_type)

    # prompt user for an input to figlet
    usr_txt = get_txt()
    print(figlet.renderText(usr_txt))

def get_txt():
    txt = input("Input: ").strip()
    return txt


def get_font(all_fonts):
    # gather the arguments passed by user
    args = sys.argv

    # Check the number of arguments
    num_args = len(args)

    # If two additional args besides file name passed by the user
    # check that the second arg is either -f or --font indicating a
    # chosen font to use when displaying the text.
    if num_args == 3:
        if args[1] in ['-f', '--font']:
            font = args[2]

            # if font is invalid, print error and exit if it does not
            if font not in all_fonts:
                sys.exit(f"EROR: '{font}' is not a valid font")

        # Print error message and exit if wrong arguments used
        else:
            sys.exit(f"ERROR: \"{args[1]}\" is not a valid flag; Use \"-f\" or \"--font\" to select a font")

    # if no args are passed except file name choose a random font
    elif num_args == 1:
        font = get_random_font(all_fonts)

    # Invalid number of arguments passed, exit
    else:
        sys.exit(f"Error: Invalid number of fonts, expected 2 arguments, recieved {num_args}.")
    return font

def get_random_font(f):
    font = random.choice(f)
    return font


if __name__ == '__main__':
    main()