"""
    CS50p Week 1, problem set 1, Home Federal Savings Bank
    In a file called bank.py, implement a program that prompts the user for a greeting.
    If the greeting starts with “hello”, output $0.
    If the greeting starts with an “h” (but not “hello”), output $20.
    Otherwise, output $100. Ignore any leading whitespace in the user's greeting,
    and treat the user's greeting case-insensitively.
"""

# prompt user for greeting and make case insensitive, and strip leading whitespace
greet = input("Please greet the customer: ").lstrip().lower()

# select the first 5 characters of the greeting
first_5char = greet[0:5]

# collect the first letter of the string
first_letter = first_5char[0]

if first_5char == "hello":
    print("$0")
elif first_letter == "h":
    print("$20")
else:
    print("$100")
