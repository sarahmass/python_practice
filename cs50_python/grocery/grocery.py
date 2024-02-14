'''
    CS50P week 3 problem set 3: Grocery List
    In a file called grocery.py, implement a program that prompts the user for items,
    one per line, until the user inputs control-d (which is a common way of ending one's
    input to a program). Then output the user's grocery list in all uppercase, sorted
    alphabetically by item, prefixing each line with the number of times the user inputted
    that item. No need to pluralize the items. Treat the user's input case-insensitively.
'''

def main():
    groceries = get_list()

    # sort the list alphabetically
    sorted_items = list(groceries.keys())
    sorted_items.sort()
    for item in sorted_items:
        print(f"{groceries[item]} {item}")

def get_list():
    # initiate list
    list = {}

    while True:
        # get grocery items
        try:
            item = input().strip().upper()
        except EOFError:
            print("")
            break
        else:
            # add items to dict or increase value
            list[item] = list.get(item, 0) + 1
    return list

main()