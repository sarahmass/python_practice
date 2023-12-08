'''
    CS50p, week 2, problem set 2: Camel case
    In a file called camel.py, implement a program that prompts the user
    for the name of a variable in camel case and outputs the corresponding
    name in snake case. Assume that the user's input will indeed be in camel case.
'''

def main():
    ''' Prompt user for a camel case variable
        return a string in snake case
    '''
    camel_case = input("Enter a variable name in camel case: ").strip()
    snake_case = transform_to_snake(camel_case)

    print(snake_case)

def transform_to_snake(camel):
    snake = ''

    # iterate through each letter and check for capital letters
    for i in range(len(camel)):
        # just in case someone capitalizes first letter
        if i == 0 and camel[i].isupper():
            snake += camel[i].lower()

        # replace any capital letter with _{letter}
        elif camel[i].isupper():
            snake += "_" + camel[i].lower()

        # lower case letters are left alone
        else:
            snake += camel[i]

    return snake

if __name__ == "__main__":
    main()