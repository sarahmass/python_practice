'''
    CS50p  Week 3 preoblem set 3: Fuel Gauge
    Fuel gauges indicate, often with fractions, just how much fuel is in a tank.
    For instance 1/4 indicates that a tank is 25% full, 1/2 indicates that a tank is 50% full,
    and 3/4 indicates that a tank is 75% full.

    In a file called fuel.py, implement a program that prompts the user for a fraction,
    formatted as X/Y, wherein each of X and Y is an integer, and then outputs, as a percentage
    rounded to the nearest integer, how much fuel is in the tank. If, though, 1% or less remains,
    output E instead to indicate that the tank is essentially empty. And if 99% or more remains,
    output F instead to indicate that the tank is essentially full.


    If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again.
    (It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError.

'''

def main():
    percent = get_percent("Fraction: ")

    if is_full(percent):
        print("F")
    elif is_empty(percent):
        print("E")
    else:
        print(f"{percent}%")



def is_full(p):
    return p >= 99

def is_empty(p):
    return p<= 1

def get_percent(prompt):
    while True:
        # handle a missing fraction
        try:
            x, y = input(prompt).split('/')

        except ValueError:
            continue

        # handle if x or y are not integers
        try:
            x, y = int(x), int(y)

        except ValueError:
            continue

        # if y is greater than x the tank is over full;
        # It does not make sense for x to be greater than y.
        if x > y:
            continue

        # handle if y is zero while calculating percenty
        try:
            p = round(100 * x / y)
        except ZeroDivisionError:
            continue

        else:
            return p

main()
