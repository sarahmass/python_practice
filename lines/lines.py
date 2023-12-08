"""
    CS50P week 6: I/O, problem set 6: Lines of Code3
    In a file called lines.py, implement a program that expects exactly one command-line argument,
    the name (or path) of a Python file, and outputs the number of lines of code in that file,
    excluding comments and blank lines. If the user does not specify exactly one command-line argument,
    or if the specified file's name does not end in .py, or if the specified file does not exist, the program
    should instead exit via sys.exit.

    Assume that any line that starts with #, optionally preceded by whitespace, is a comment.
    (A docstring should not be considered a comment.) Assume that any line that only contains whitespace is blank.
"""

import sys
import os


def main():
    path = check_args(sys.argv)
    lines = count_lines(path)
    print(lines)


def check_args(args):
    # count args
    num_args = len(args)

    # if not enough args, print msg and sys.exit
    if num_args < 2:
        sys.exit("Too few command-line arguments")

    # if too many args, print msg and sys.exit
    elif num_args > 2:
        sys.exit("Too many command-line arguments")

    # correct number of args now check file and path
    else:
        file_path = args[1]
        if not is_python(file_path):
            sys.exit("Not a Python file")

        elif not file_exists(file_path):
            sys.exit("File does not exist")

        else:
            return file_path


def count_lines(path):
    with open(path, 'r') as f:
        all_lines = f.readlines()
    cmt_lines = 0
    blank_lines = 0

    line_count = 0
    for line in all_lines:
        if line.lstrip().startswith("#"):
            cmt_lines += 1
            continue
        elif line.isspace() or len(line.strip()) == 0:
            blank_lines += 1
            continue
        else:
            line_count += 1

    # print(f"blank lines: {blank_lines}")
    # print(f"Lines of comments: {cmt_lines}")
    return line_count



def is_python(file):
    _ , ext = os.path.splitext(file)
    return ext == ".py"

def file_exists(file):
    return os.path.isfile(file)

if __name__ == "__main__":
    main()