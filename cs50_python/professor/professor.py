"""
    CS50p week 4 problem set 4: Little professor
    In a file called professor.py, implement a program that:

        * Prompts the user for a level,
            ** If the user does not input 1, 2, or 3, the program should prompt again.

        * Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y
          is a non-negative integer with 'level' digits.
          No need to support operations other than addition (+).

        * Prompts the user to solve each of those problems. If an answer is not correct (or not even a number),
          the program should output EEE and prompt the user again, allowing the user up to three tries in total
          for that problem. If the user has still not answered correctly after three tries, the program should
          output the correct answer.

        * The program should ultimately output the user’s score: the number of correct answers out of 10.

        Structure your program as follows, wherein get_level prompts (and, if need be, re-prompts) the user for
        a level and returns 1, 2, or 3, and generate_integer returns a randomly generated non-negative integer
        with level digits or raises a ValueError if level is not 1, 2, or 3:
"""


import random


def main():
    level = get_level()
    score = 0

    # produce and score 10 problems
    for _ in range(10):
        X = generate_integer(level)
        Y = generate_integer(level)
        score += get_check_sum(X, Y)

    # print the number of correct answers
    print(f"Score: {score}")


def get_level():
    # prompt user for input until a valid level is returned
    while True:
        lvl = input("Level: ")
        try:
            lvl = int(lvl)
        except ValueError:
            continue
        if 1 <= lvl <= 3:
            return lvl


def generate_integer(level):
    # generate single digit number
    if level == 1:
        upper = 9
        lower = 0

    # generate 2 digit number
    elif level == 2:
        upper = 99
        lower = 10

    # generate 3 digit number
    elif level == 3:
        upper = 999
        lower = 100

    # Raise error if level is invalid
    else:
        raise ValueError

    return random.randint(lower, upper)


def get_check_sum(x, y):
    # each sum gets three tries
    tries = 3

    # prompt user for solution to sum at most 3 times
    while tries > 0:
        ans = input(f"{x} + {y} = ")
        tries -= 1

        # Error and uses up a try if not a valid integer
        try:
            ans = int(ans)
        except ValueError:
            print("EEE")
            continue

        # return a score of 1 if answer is correct
        if ans == x + y:
            return 1

        # print EEE to indicate it was an incorect answer
        else:
            print("EEE")
            continue

    # after three invalid/incorrect answer print answer
    # and get a score of zero for the problem
    print(f"{x} + {y} = {x + y}")
    return 0


if __name__ == "__main__":
    main()
