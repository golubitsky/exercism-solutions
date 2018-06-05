import datetime
from calendar import monthrange
import re


class MeetupDayException(Exception):
    def __init__(self, message):
        super().__init__(message)


days = {"Monday": 0,
        "Tuesday": 1,
        "Wednesday": 2,
        "Thursday": 3,
        "Friday": 4,
        "Saturday": 5,
        "Sunday": 6}


def meetup_day(year, month, day_of_the_week, which):
    start_weekday, days_in_month = monthrange(year, month)

    if which == 'teenth':
        for day in range(13, 20):
            date = datetime.date(year, month, day)
            if date.weekday() == days[day_of_the_week]:
                return date
    elif which == 'last':
        for day in reversed(range(1, days_in_month+1)):
            date = datetime.date(year, month, day)
            if date.weekday() == days[day_of_the_week]:
                return date
    else:
        target_day = int(re.search('\d', which)[0])
        days_found = 0
        for day in range(1, days_in_month+1):
            date = datetime.date(year, month, day)
            if date.weekday() == days[day_of_the_week]:
                days_found += 1
            if days_found == target_day:
                return date

    raise MeetupDayException('.+')
