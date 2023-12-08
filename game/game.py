"""
    CS50P Week 4, problem set 4: Guessing Game
    In a file called game.py, implement a program that:

        Prompts the user for a level,
         If the user does not input a positive integer, the program should prompt again.

        Randomly generates an integer between 1 and
          inclusive, using the random module.

        Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
        If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
        If the guess is larger than that integer, the program should output Too large! and prompt the user again.
        If the guess is the same as that integer, the program should output Just right! and exit.
"""
import random


def main():
    level = get_level()
    number = get_random_number(level)
    get_and_check_guess(number)


def get_level():
    # prompt user for an input
    while True:
        l = input("Level: ").strip()

        # Check if the integer is  a positive integer
        try:
            l = int(l)
        except ValueError:
            continue
        if l > 0:
            return l


def get_random_number(lvl):
    # choose a random int between 1 and level
    n = random.randint(1, lvl)
    return n


def get_and_check_guess(num):
    while True:
        g = input("Guess: ")
        try:
            g = int(g)
        except ValueError:
            continue
        if g < 1:
            continue
        elif g == num:
            print("Just right!")
            break
        elif g > num:
            print("Too large!")
            continue
        elif g < num:
            print("Too small!")
            continue


if __name__ == "__main__":
    main()
