'''
    CS50p, Week 1, deep thought
        In deep.py, implement a program that prompts the user for the answer
        to the Great Question of Life, the Universe and Everything, outputting
        Yes if the user inputs 42 or (case-insensitively) forty-two or forty two.
        Otherwise output No.
'''

answer = input("What is the answer to the Great Question of Life, the Universe, and Everything? ")
# make case insensitive and stripaway white space
answer = answer.lower().strip()

# check the three cases:
if answer == "42" or answer == "forty-two" or answer == "forty two":
    print("Yes")
else:
    print("No")

