import datetime


def add_gigasecond(birth_date):
    gigasecond = 1_000_000_000

    return birth_date + datetime.timedelta(seconds=gigasecond)
