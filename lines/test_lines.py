import sys

def main():
    while True:
        fraction_string = get_input()
        try:
            percent = convert(fraction_string)
        except ValueError:
            continue
        except ZeroDivisionError:
            continue

        else:
            gauge_reading = gauge(percent)
            break
    print(gauge_reading)




def convert(fraction):
    '''
        the input, fraction, is a str in "X/Y" format,
        X and Y are integers,
        returns a percentage rounded to the nearest int between 0 and 100, inclusive.

        Error Handling:
        - If X and/or Y is not an integer, or if X is greater than Y,
            then convert should raise a ValueError.
        - If Y is 0, then convert should raise a ZeroDivisionError.
    '''
    if type(fraction) != str:
        raise TypeError

    # make sure fraction contains a fraction
    if "/" not in fraction:
        raise ValueError

    # parse x and y from fraction
    else:
        x, y = fraction.split("/")

    # make sure that x and y are integers
    if not (x.isdigit() and y.isdigit()):
        raise ValueError

    # Change the type() for x and y to str
    else:
        x, y = int(x), int(y)

    # do not divide by zero
    if y == 0:
        raise ZeroDivisionError

    # Make sure that 0 <= fraction <= 1
    if y < x:
        raise ValueError



    # No negative integers
    if x < 0 or y < 0:
        raise ValueError

    # calculate the positive integer percetage
    percent = round(100 * x / y)

    return percent



def get_input():
    while True:
        # propt user for a fraction
        x_div_y = input("Fraction: ").strip()
        if "/" in x_div_y:
            return x_div_y


def gauge(percentage):
    '''
        gauge expects an int and returns a str that is:
        - "E" if that int is less than or equal to 1,
        - "F" if that int is greater than or equal to 99,
        - and "Z%" otherwise, wherein Z is that same int.
    '''
    if type(percentage) != int:
        raise TypeError

    if percentage > 100 or percentage < 0:
        raise ValueError

    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"


def is_full(p):
    return p >= 99

def is_empty(p):
    return p<= 1



if __name__ == "__main__":
    main()