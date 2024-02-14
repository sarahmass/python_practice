'''
    CS50p Week 0, problem set 0: Making faces.
    The Setup: Before there were emoji, there were emoticons, whereby text like :)
    was a happy face and text like :( was a sad face. Nowadays, programs tend to
    convert emoticons to emoji automatically!

    Task: In a file called faces.py, implement a function called convert that accepts
    a str as input and returns that same input with any :) converted to 🙂 (otherwise
    known as a slightly smiling face) and any :( converted to 🙁 (otherwise known as a
    slightly frowning face). All other text should be returned unchanged.

    Then, in that same file, implement a function called main that prompts the user for input,
    calls convert on that input, and prints the result. You are welcome, but not required,
    to prompt the user explicitly, as by passing a str of your own as an argument to input.
    Be sure to call main at the bottom of your file.
'''

def convert(text):
    '''
    input: str
    function: remove emoticons for happy and sad face and convert
        to emojis.
    return: str
    '''
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

def main():
    '''
        propt user for a statement and encourage emodicons
        convert emodicons to emojis
        print the user's statement with emojis
    '''
    input_text = input("Enter a statement and I will transform your emodicons into emojis: ")
    input_text = convert(input_text)
    print(input_text)

main()