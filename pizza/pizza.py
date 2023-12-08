"""
    CS50P week 6: I/O problem set 6: Pizza PY
    In a file called pizza.py, implement a program that expects exactly one command-line argument,
    the name (or path) of a CSV file in Pinocchio's format, and outputs a table formatted as ASCII
    art using tabulate, a package on PyPI at pypi.org/project/tabulate. Format the table using the
    library's grid format. If the user does not specify exactly one command-line argument, or if
    the specified file's name does not end in .csv, or if the specified file does not exist, the
    program should instead exit via sys.exit.

    wget https://cs50.harvard.edu/python/2022/psets/6/pizza/sicilian.csv
    wget https://cs50.harvard.edu/python/2022/psets/6/pizza/regular.csv

"""

import os
import sys
import csv
from tabulate import tabulate

def main():
    path = check_args(sys.argv)
    table = get_table(path)
    print(table)

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

        if not is_csv(file_path):
            sys.exit("Not a CSV file")

        elif not file_exists(file_path):
            sys.exit("File does not exist")

        else:
            return file_path

def get_table(path):
    lines = []
    with open(path) as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            lines.append(row)

        table = tabulate(lines, tablefmt="grid", headers="firstrow")
        return table

def is_csv(file):
    _ , ext = os.path.splitext(file)
    return ext == ".csv"

def file_exists(file):
    return os.path.isfile(file)

if __name__ == "__main__":
    main()
