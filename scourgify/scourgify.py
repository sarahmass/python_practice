"""
    CS50 week 6: I/O problem set 6: Scourgify

    In a file called scourgify.py, implement a program that:

        - Expects the user to provide two command-line arguments:
            -- the name of an existing CSV file to read as input,
                with columns: name and house
            -- the name of a new CSV to write as output,
                with columns first, last, and house.
        - Converts that input to that output, splitting each name into a first name and last name.
          Assume that each student will have both a first name and last name.
        - If the user does not provide exactly two command-line arguments, or if the first cannot be read,
          the program should exit via sys.exit with an error message.
"""

import os
import sys
import csv

def main():
    inpath, outpath = check_args(sys.argv)
    after = convert_csv(inpath)
    write_csv(after, outpath)

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

        if not is_csv(read_path):
            sys.exit("Not a CSV file")

        elif not file_exists(read_path):
            sys.exit("File does not exist")

        else:
            return read_path, write_path

def is_csv(file):
    _ , ext = os.path.splitext(file)
    return ext == ".csv"

def file_exists(file):
    return os.path.isfile(file)

def convert_csv(path):
    after = []
    with open(path) as before:
        #fieldnames = ["name", "house"]
        reader = csv.DictReader(before,)

        for row in reader:
            name = row["name"].strip()
            house = row["house"].strip()

            last, first = name.strip().split(",")
            after.append(
                {
                    "first" : first.strip(),
                    "last" : last.strip(),
                    "house" : house.strip()
                }
            )

        return after

def write_csv(cln_list, path):
    with open(path, "w") as after:
        fieldnames = ["first", "last", "house"]
        writer = csv.DictWriter(after, fieldnames=fieldnames)

        writer.writeheader()
        for row in cln_list:
            writer.writerow(row)


if __name__ == "__main__":
    main()
