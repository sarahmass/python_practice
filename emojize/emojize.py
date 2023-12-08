"""
    CS50p Week 4 problem set 4: Emojize

    In a file called emojize.py, implement a program that prompts the
    user for a str in English and then outputs the “emojized” version of that str,
    converting any codes (or aliases) therein to their corresponding emoji

"""


import emoji


def main():
    phrase = get_phrase()
    phrase_emojized = emoji.emojize(phrase, language="en")
    print(f"Output: {phrase_emojized}")


def get_phrase():
    p = input(f"Input: ").strip()
    return p


if __name__ == "__main__":
    main()
