"""
    CS50P week 5 problem set 5: test bank
    rewrite problem set 1's bank:
    --- CS50p Week 1, problem set 1, Home Federal Savings Bank
        In a file called bank.py, implement a program that prompts the user for a greeting.
        If the greeting starts with “hello”, output $0.
        If the greeting starts with an “h” (but not “hello”), output $20.
        Otherwise, output $100. Ignore any leading whitespace in the user's greeting,
        and treat the user's greeting case-insensitively.
"""



def main():
    # prompt user for greeting and make case insensitive, and strip leading whitespace
    greet = input("Greeting: ").lstrip().lower()

    payout = value(greet)

    print(f"${payout}")



def value(greeting):
    greeting = greeting.lstrip().lower()
    print(greeting[0:5])
    # check that there is a greeting:
    if len(greeting) == 0:
        return 100

    # check the first 5 characters are 'hello'
    elif greeting[0:5] == "hello":
        return 0

    # check to see if the first character is an 'h'
    elif greeting[0] == "h":
        return 20

    # not 'hello' and doesn't start with 'h'
    else:
        return 100



if __name__ == "__main__":
    main()