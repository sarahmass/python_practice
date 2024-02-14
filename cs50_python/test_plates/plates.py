"""
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


"""


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

    # If all Letters break early
    if is_alpha(s):
        return True

    # first two characters must be letters
    if not is_alpha(s[0:2]):
        return False

    # No periods, spaces or punctuation so check for Alpha numeric
    if not is_alpha_numeric(s):
        return False

    # once a number occurs the rest have to be numbers
    if not is_valid_num_placement(s):
        return False

    return True


def is_correct_length(l):
    return 2 <= l <= 6


def is_alpha_numeric(string):
    return string.isalnum()


def is_alpha(string):
    return string.isalpha()


def is_valid_num_placement(string):
    # at this point we know that the length is correct
    # we know that the first two characters are letters
    # we know it is alpha-numeric with at least one number
    # Now find first digit and make sure it isn't in middle
    # of vowels nor a zero.

    num_digits = 0
    str_len = len(string)

    for idx, char in enumerate(string):
        num_digits += char.isdigit()

        # find first digit if any
        if num_digits == 1:
            # First Digit can't be zero
            if char == "0":
                return False

            # all the rest of the characters have to be digits or
            # this is the last character.
            if not string[idx::].isdigit() and idx != str_len - 1:
                return False

            # first digit is not zero,
            # rest of characters are digits, or
            # or no more characters
            else:
                return True






if __name__ == "__main__":
    main()
