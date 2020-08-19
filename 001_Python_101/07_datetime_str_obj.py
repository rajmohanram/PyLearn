from datetime import datetime
from dateutil import rrule

# convert datetime string to datetime object
def convert_date_obj(d):
    d_obj = datetime.strptime(d, '%d-%m-%Y')
    return d_obj


date_time_str = "18-08-2020"
print(f'Datetime string: {date_time_str}')
date_time_obj = convert_date_obj(date_time_str)
print(f'Datetime object: {date_time_obj}')
print(f'Datetime string: {date_time_obj.strftime("%d-%m-%Y")}')


# find difference between 2 dates (xw yd
def date_diff(d1, d2):
    d_obj1 = convert_date_obj(d1)
    d_obj2 = convert_date_obj(d2)
    total_days = (d_obj1 - d_obj2).days
    weeks = int(total_days / 7)
    days = abs(total_days) % 7
    print(f'{weeks}w {days}d')


date_time_str1 = "22-08-2020"
date_time_str2 = "23-08-2020"
date_diff(date_time_str1, date_time_str2)