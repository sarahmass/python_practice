''' CS50p Week 0, Problem Set 0: Tip Calculator
    Main is already written, but finish dollars_to_float and
    percent_to_float.
'''


def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # strip $ sign
    d = d.strip('$')
    # convert the d to a float
    d = float(d)
    return float(d)

def percent_to_float(p):
    # strip away percent symbol
    p = p.strip('%')
    # convert a percent to a float in decimal equivalent
    p = float(p)/100
    return p


main()