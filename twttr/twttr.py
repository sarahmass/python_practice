'''
    CS50p week 2 problem set 2: Just Setting Up My Twitter
    When texting or tweeting, it's not uncommon to shorten words to save time or space,
    as by omitting vowels, much like Twitter was originally called twttr. In a file called
    twttr.py, implement a program that prompts the user for a str of text and then outputs
    that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in
    uppercase or lowercase.
'''

def main():
    # get text/tweet
    tweet = input("Input a str of text: ").strip()

    twt = ''
    # check for vowels:
    for letter in tweet:
        if not isvowel(letter):
            twt += letter
    print(twt)

def isvowel(l):
    vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
    return l in vowels

if __name__ == "__main__":
    main()