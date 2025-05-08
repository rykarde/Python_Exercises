month = int(input("Enter a month (1-12): "))
is_month_even = month == 4 or month == 6 or month == 9 or month == 11

if month < 1 or month > 12:
    print("Error. Month must be between 1 and 12.")

day = int(input("Enter a day: "))

if is_month_even and (day < 1 or day > 30):
    print("Error. Day must be between 1 and 30.")

if not is_month_even and (day < 1 or day > 31):
    print("Error. Day must be between 1 and 31.")

year = int(input("Enter your birth year: "))

if 1000 > year or year > 9999:
    print("Error. Year must have four digits")

