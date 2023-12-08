'''
    CS50p week 5 problem set 5: test_twttr
    but first I need to reimplement twttr.py to have the shorten function
    as described in the assignment.
    So the main funtion uses the shorten functen to remove the vowels.

'''


def main():
    word = input("Input: ").strip()
    shrt_wrd = shorten(word)
    print(f"Output: {shrt_wrd}")


def shorten(word):
    short_word = ''
    for lttr in word:
        if lttr.lower() not in ["a", "e", "i", "o", "u"]:
            short_word += lttr
    return short_word



if __name__ == "__main__":
    main()