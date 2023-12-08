'''
    CS50p week 1 problemset 1: Math interpreter
    In a file called interpreter.py, implement a program that prompts the user
    for an arithmetic expression and then calculates and outputs the result as a
    floating-point value formatted to one decimal place. Assume that the user's
    input will be formatted as x y z, with one space between x and y and one space
    between y and z, wherein:

        x is an integer
        y is +, -, *, or /
        z is an integer
'''

def add(a,b):
    return float(a + b)

def subtract(a,b):
    return float(a - b)

def multiply(a,b):
    return float(a * b)

def divide(a,b):
    return float(a / b)

def main():
    # get expression
    expression = input("Enter your expression: ").strip().lower()
    x, y, z = expression.split(" ")
    x = int(x)
    z = int(z)

    if y == "+":
        print(f"{add(x,z)}")
    elif y == '-':
        print(f"{subtract(x,z)}")
    elif y == '*':
        print(f"{multiply(x,z)}")
    elif y == '/' and z != 0:
        print(f"{divide(x,z):.1f}")
    else:
        print(f"The expression, {expression}, is invalid.")

main()