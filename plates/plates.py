'''
    CS50p week 2 problem set 2: Vanity plates
    In Massachusetts, home to Harvard University, it's possible to request a vanity license
    plate for your car, with your choice of letters and numbers instead of random ones. Among
    the requirements, though, are:

        - “All vanity plates must start with at least two letters.”
        - “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
        - “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an
            acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a '0'.”
        - “No periods, spaces, or punctuation marks are allowed.”

    In plates.py, implement a program that prompts the user for a vanity plate and then output Valid if meets all of
    the requirements or Invalid if it does not. Assume that any letters in the user's input will be uppercase. Structure
    your program per the below, wherein is_valid returns True if s meets all requirements and False if it does not.
    Assume that s will be a str. You're welcome to implement additional functions for is_valid to call (e.g., one function per requirement).


'''

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    length = len(s)

    # length must be between 2 and 6 characters
    if not is_correct_length(length):
        return False

    # No periods, spaces or punctuation so check for Alpha numeric
    if not is_alpha_numeric(s):
        return False

    # first two characters must be letters
    if not is_alpha(s[0:2]):
        return False

    # once a number occurs the rest have to be numbers
    if not is_no_letter_after_number(s[2::]):
        return False

    return True


def is_correct_length(l):
    return 2 <= l <= 6

def is_alpha_numeric(string):
    return string.isalnum()

def is_alpha(string):
    return string.isalpha()

def is_no_letter_after_number(string):
    for i in range(len(string) - 1):
        if string[i].isdigit():
            return string[i::].isdigit() and string[i] != '0'
    return True


main()