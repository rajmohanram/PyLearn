from datetime import datetime, timedelta

# Today's date in yyyy-mm-dd
curr_datetime = datetime.now()
curr_date = curr_datetime.date()
print("Today's date:", curr_date)

# strftime - String from Time - Convert time to string in desired format
# https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior

# Change date format to dd-mm-yyy
date_format1 = curr_date.strftime("%d-%m-%Y")
print("Today's date:", date_format1)

# Change date format to dd-mmm-yyy
date_format2 = curr_date.strftime("%d-%B-%Y")
print("Today's date:", date_format2)

# Date N days ago
N = 3
time_diff = timedelta(days=N, hours=0, minutes=0)

date_N_days_ago = curr_datetime - time_diff
print("Date", N, "days ago is", date_N_days_ago.strftime("%d-%B-%Y"))

# Date N days after
N = 5
time_diff = timedelta(days=N, hours=0, minutes=0)

date_N_days_after = curr_datetime + time_diff
print("Date", N, "days after is", date_N_days_after.strftime("%d-%B-%Y"))
