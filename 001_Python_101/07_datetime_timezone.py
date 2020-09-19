# this exercise required installing pytz package - pip install pytz
from datetime import datetime, timedelta
import pytz

# print a list of all timezone
print("Timezone list:", pytz.all_timezones)

# datetime object - in your timezone
curr_datetime = datetime.now()
print("Current datetime in your timezone:", curr_datetime.strftime("%d-%m-%Y %H:%M:%S"))


# datetime object - in the required timezone - Pick some timezone from the timezone list
tz_name = "US/Pacific"
required_tz = pytz.timezone(tz_name)
datetime_required_tz = datetime.now(required_tz)
curr_datetime = datetime.now()
print("Current datetime in", tz_name, "timezone:", datetime_required_tz.strftime("%d-%m-%Y %H:%M:%S"))
