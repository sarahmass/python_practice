'''
    CS50p week 3 problem set 3: Outdated:
        In a file called outdated.py, implement a program that prompts the user for a date,
        anno Domini, in month-day-year order, formatted like 9/8/1636 or September 8, 1636,
        wherein the month in the latter might be any of the values in the months dictionary below:

        Then output that same date in YYYY-MM-DD format. If the user's input is not a valid date in
        either format, prompt the user again. Assume that every month has no more than 31 days; no
        need to validate whether a month has 28, 29, 30, or 31 days.
'''

months = {
      "January": "01",
      "February": "02" ,
      "March": "03",
      "April": "04",
      "May": "05",
      "June": "06",
      "July": "07",
      "August": "08",
      "September": "09",
      "October": "10",
      "November": "11",
      "December": "12",
}

def main():
    month, day, year = get_date()
    print(f"{year}-{month}-{day}")

def get_date():
    # prompt user for input
    is_valid_date = False
    while not is_valid_date:
        # prompt user for input
        date = input("Date: ").strip().title()
        # parse date if in mm/dd/yyyy format:
        if "/" in date:
            try:
                m, d, y = date.split("/")
            except ValueError:
                continue
            # make sure that m in this format is a digit
            if not m.isdigit():
                continue
        else:
            try:
                m, d, y = date.split(" ")
            except ValueError:
                continue
            # month should be alpha, day should have a comma
            if (not m.isalpha()) or (d[-1] != ","):
                continue

        mm = get_month(m)
        dd = get_day(d.strip(','))
        yyyy = get_year(y)

        is_valid_date = mm and dd and yyyy

    return mm, dd, yyyy

def get_month(m):
    # check if m is one of the keys in mongths and
    # return the months two digit zero-padded numerical value
    for k,v in months.items():
        if m in [k, str(int(v)), v]:
            return v

    return False

def get_day(d):
    # try to get int representation of day
    try:
        d = int(d)
    except ValueError:
        return False
    else:
        # zero pad if singe digit an make sure in range of [1,32)
        if d in range(1,32):
            return f"{d:02}"
        else:
            return False

def get_year(y):
    # try to get valid int rpresentation of year
    try:
        y = int(y)
    except ValueError:
        return False
    else:
        # check that y in [0,9999] and padd with
        # to make a four digit year.
        if y in range(10000):
            num_zero_pad = 4 - len(str(y))
            return f"{y:04}"
        else:
            return False


main()
