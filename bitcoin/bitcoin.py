"""
    CS50p week 4 problem set 4: BitCoin Price index
        Bitcoin is a form of digitial currency, otherwise known as cryptocurrency. Rather than rely on a central
        authority like a bank, Bitcoin instead relies on a distributed network, otherwise known as a blockchain,
        to record transactions.

        Because there's demand for Bitcoin (i.e., users want it), users are willing to buy it, as by exchanging
        one currency (e.g., USD) for Bitcoin.

        In a file called bitcoin.py, implement a program that:

        * Expects the user to specify as a command-line argument the number of Bitcoins that they would like to buy.

        * If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.

        * Queries the API for the CoinDesk Bitcoin Price Index at https://api.coindesk.com/v1/bpi/currentprice.json,
          which returns a JSON object, among whose nested keys is the current price of Bitcoin as a float.

        * Be sure to catch any exceptions, as with code like:
                import requests

                try:
                    ...
                except requests.RequestException:

        * Outputs the current cost of Bitcoins in USD to four decimal places, using , as a thousands separator.


"""

import sys
import requests



def main():
    num_of_coins = get_number_of_coins()
    price_per_coin = get_price_per_coin()
    cost = num_of_coins * price_per_coin

    # print cost with commas separating 1000s and 4 decimal places
    print(f"${cost:,.4f}")

def get_number_of_coins():
    args = sys.argv
    if len(args) < 2:
        sys.exit("Missing command-line argument")

    try:
        return float(args[1].strip())

    except ValueError:
        sys.exit("Command-line argument is not a number")



def get_price_per_coin():
    # request information from CoinDesk:
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    except requests.RequestException as err:
        sys.exit(err)

    # convert to dictionary format
    rate = response.json()['bpi']['USD']['rate_float']
    return rate

if __name__ == "__main__":
    main()
