'''
    CS50p problem set 0: Playback Speed
    The set up:  Some people have a habit of lecturing speaking rather quickly,
    and it would be nice to slow them down, a la playback speed = 0.75 on YouTube,
    or even by having them pause between words.

    The Goal: in a file called playback.py, implement a program in Python that
    prompts the user for input and then outputs that same input, replacing each
    space with ... (i.e., three periods).
'''

# Get a phrase from the user:
text = input("Enter a phrase and I will help you communicate at a slower pace: ")

# using the replace() method replace all spaces with ...
text = text.replace(' ', '...')
print(text)