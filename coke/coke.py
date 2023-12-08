"""
    CS50p week 2 problem set 2: Coke Machine:
    Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and
    only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.

    In a file called coke.py, implement a program that prompts the user to insert
    a coin, one at a time, each time informing the user of the amount due. Once the
    user has inputted at least 50 cents, output how many cents in change the user
    is owed. Assume that the user will only input integers, and ignore any integer
    that isn't an accepted denomination.
"""


def main():
    amount_deposited = 0
    while amount_deposited < 50:
        coin_deposited = int(input("Insert Coin: "))

        # if valid coin add to amount deposited
        if isvalid(coin_deposited):
            amount_deposited += coin_deposited
        amount_due = 50 - amount_deposited

        # amount due is printed if 50 cents isn't reached
        if amount_due > 0:
            print(f"Amount Due: {amount_due}")

        # if amount_deposited is greater than or equal to 50
        # amount_due will be negative so report change due
        else:
            print(f"Change Owed: {abs(amount_due)}")


def isvalid(coin):
    if coin in [5, 10, 25]:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
