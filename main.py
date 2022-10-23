from typing import Dict


# https://www.codewars.com/kata/52742f58faf5485cae000b9a/train/python

def format_duration(seconds):
    list_of_durations: dict[str, int] = {
        "minute": 60,
        "hour": 60 * 60,
        "day": 24 * 3600,
        "year": 24 * 3600 * 365
    }

    result = ''
    word_ending = ''

    # less than 1 hour but more than 1 minute
    if list_of_durations["minute"] <= seconds < list_of_durations["hour"]:
        return

    # greater than 1 hour (DONE)
    if list_of_durations["hour"] <= seconds < list_of_durations["day"]:
        # hours
        if seconds / list_of_durations["hour"] >= 2:
            word_ending = 's'
        result = f'{int(seconds / list_of_durations["hour"])} hour{word_ending}'
        word_ending = ''
        # minutes
        if seconds % list_of_durations["hour"] / 60 >= 1:
            if seconds % list_of_durations["hour"] / 60 >= 2:
                word_ending = 's'
            result += f', {int(seconds % list_of_durations["hour"] / 60)} minute{word_ending}'
        word_ending = ''
        # seconds
        if seconds % list_of_durations["hour"] % list_of_durations["minute"] != 0:
            if seconds % list_of_durations["hour"] % list_of_durations["minute"] > 1:
                word_ending = 's'
            result += f' and {seconds % list_of_durations["hour"] % list_of_durations["minute"]} second{word_ending}'
        return result

    # days should be here

    # TODO : I have a problem identifying the HOURS correctly
    # if seconds value less than inf and greater than day, i.e. years
    if list_of_durations["day"] <= seconds < list_of_durations["year"]:
        # days
        if seconds / list_of_durations["day"] >= 2:
            word_ending = 's'
        result += f'{int(seconds / list_of_durations["day"])} day{word_ending}'
        word_ending = ''
        # hours
        if seconds > list_of_durations['hour']:
            if seconds / list_of_durations["hour"] >= 2:
                word_ending = 's'
            result += f', {int(seconds / list_of_durations["hour"])} hour{word_ending}'
        word_ending = ''
        # minutes
        if seconds % list_of_durations["hour"] / 60 >= 1:
            if seconds % list_of_durations["hour"] / 60 >= 2:
                word_ending = 's'
            result += f', {int(seconds % list_of_durations["hour"] / 60)} minute{word_ending}'
        word_ending = ''
        # seconds
        if seconds % list_of_durations["hour"] % list_of_durations["minute"] != 0:
            if seconds % list_of_durations["hour"] % list_of_durations["minute"] > 1:
                word_ending = 's'
            result += f' and {seconds % list_of_durations["hour"] % list_of_durations["minute"]} second{word_ending}'
        return result


print(format_duration(1))  # 1 second
print(format_duration(62))  # 1 minute and 2 seconds
print(format_duration(120))  # 2 minutes
print(format_duration(3600))  # 1 hour
print(format_duration(7264))  # 2 hours, 1 minute and 4 seconds
print(format_duration(75454681))  # 2 years, 2919 hours, 26 minutes and 39 seconds
print(format_duration(10509999))  # 121 days, 15 hours, 26 minutes and 38 seconds
