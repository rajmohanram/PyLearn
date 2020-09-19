# A sample program to get the number of days in a month
# Uses function to get the result


# Number of days per month. First value is placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    """Return True for leap years, False for non-leap years."""

    return year % 4 == 0 and (year % 100 !=0 or year % 400 == 0)


def days_in_month(year, month):
    """Return number of days in the month in that year."""

    if not 1 <= month <=12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]


if __name__ == "__main__":
    year_input = int(input("Enter the year:"))
    month_input = int(input("Enter the month as number:"))
    
    print(days_in_month(year_input, month_input))
