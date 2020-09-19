from datetime import datetime, timedelta

# datetime object
curr_datetime = datetime.now()
print("Current datetime:", curr_datetime.strftime("%d-%m-%Y %H:%M:%S"))

# datetime N days ago
d = 3
h = 0
m = 0
time_diff = timedelta(days=d, hours=h, minutes=m)
past_datetime = curr_datetime - time_diff
print("Previous datetime is ", past_datetime.strftime("%d-%m-%Y %H:%M:%S"))

# datetime N days after
d = 3
h = 0
m = 0
time_diff = timedelta(days=d, hours=h, minutes=m)
future_datetime = curr_datetime + time_diff
print("Future datetime is ", future_datetime.strftime("%d-%m-%Y %H:%M:%S"))

# Difference between datetime objects
time_diff = future_datetime - curr_datetime
print("Difference between today and future:", time_diff)