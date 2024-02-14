'''
    Assignment 1 for CS50p:
    Indoor Voice:
                WRITING IN ALL CAPS IS LIKE YELLING
                Best to use your “indoor voice” sometimes, writing entirely in lowercase.
                Goal: In a file called indoor.py, implement a program in Python that prompts
                the user for input and then outputs that same input in lowercase. Punctuation
                and whitespace should be outputted unchanged.
                You are welcome, but not required, to prompt the user explicitly, as by
                passing a str of your own as an argument to input.
'''

# get input from the user
text = input("Enter in a phrase and I will help you to communicate without yelling: ")

# edit the input text to be all lowercase
text = text.lower()
print(text)