from datetime import datetime, timedelta

# datetime object
curr_datetime = datetime.now()
curr_time = curr_datetime.time()
print("Current time:", curr_time)
print("Current time:", curr_time.strftime("%H:%M:%S"))

# Time N hours ago
N = 3
time_diff = timedelta(days=0, hours=N, minutes=0)

time_N_hours_ago = curr_datetime - time_diff
print("Time", N, "hours ago is ", time_N_hours_ago.strftime("%H:%M:%S"))

# Time N hours after
N = 5
time_diff = timedelta(days=0, hours=N, minutes=0)

time_N_hours_after = curr_datetime + time_diff
print("Time", N, "hours after is ", time_N_hours_after.strftime("%H:%M:%S"))

