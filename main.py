# https://www.codewars.com/kata/52742f58faf5485cae000b9a/train/python
def format_duration(seconds):
    result = ''
    year = 24 * 3600 * 365 # 31536000
    day = 24 * 3600 # 86400
    hour = 60 * 60 # 3600
    minute = 60 # 60
    remainder_year = seconds - seconds % year
    remainder_day = seconds - seconds % day
    remainder_hour = seconds - seconds % hour
    remainder_minute = seconds - seconds % minute
    remainder_second = seconds
    # TODO : two iterations: at the first we get the right format (without commas and "and"), the second: add separations syntax (we can understand using arrays)
    # TODO : Remake script using reminders
    i = 0
    while(i != 2):
        # years
        if seconds >= year:
            remainder = seconds - (seconds - seconds % year)
            result += f'{int(seconds / year)} year{"s" if seconds / year >= 2 else ""}{", " if isinstance(seconds / year, float) else ""}'
            # print(f"Total time: {seconds}. At the end of the year part, left time (2 years): {remainder_year}. \nRemainder: {remainder}. Remainder should be: {143 * day + 7 * hour + 38 * minute + 1}")
        # days
        if seconds >= day:
            remainder = seconds - remainder_day
            result += f'{" and " if isinstance(seconds / day, int) else ""}{int(seconds / day) - int(seconds / year) * 365} day{"s" if seconds / day >= 2 else ""}'
            # print(f"Total time: {seconds}. At the end of the year part, left time: {remainder_day}. \nRemainder: {remainder}. Remainder should be: {143*day+7*hour+38*minute+1}") # should be 86400
        # hours
        if seconds >= hour:
            remainder = seconds - remainder_hour
            result += f'{" and " if isinstance(seconds % day / hour, int) else ""}{int(seconds % day / hour)} hour{"s" if seconds % day / hour > 1 else ""}'
            # print(f"Total time: {seconds}. At the end of the year part, left time: {remainder_hour}. \nRemainder: {remainder}. Remainder should be: {143*day+7*hour+38*minute+1}")
        # minutes
        if seconds % hour / 60 >= 1:
            remainder = seconds - remainder_minute
            result += f'{" and " if isinstance(seconds % hour / 60, int) else ""}{int(seconds % hour / 60)} minute{"s" if seconds % hour / 60 >= 2 else ""}'
            # print(f"Total time: {seconds}. At the end of the year part, left time: {remainder_minute}. \nRemainder: {remainder}. Remainder should be: {143 * day + 7 * hour + 38 * minute + 1}")
        # seconds
        if seconds % hour % minute != 0:
            remainder = seconds - remainder_second
            result += f'{" and " if isinstance(seconds % hour % minute, int) else ""}{int(seconds % hour % minute)} second{"s" if seconds % hour % minute > 1 else ""}'
            # print(f"Total time: {seconds}. At the end of the year part, left time: {remainder_second}. \nRemainder: {remainder}. Remainder should be: {143 * day + 7 * hour + 38 * minute + 1}")
        i += 1
    return f"@@@@@@ OUTPUT RESULT: {result}"


print(format_duration(1))  # 1 second
print(format_duration(62))  # 1 minute and 2 seconds
print(format_duration(120))  # 2 minutes
print(format_duration(3600))  # 1 hour
print(format_duration(7264))  # 2 hours, 1 minute and 4 seconds
print(format_duration(90000))  # 1 day and 1 hour
print(format_duration(10509999))  # 121 days, 15 hours, 26 minutes and 39 seconds
print(format_duration(2*24 * 3600 * 365))
print(format_duration(75454681))  # 2 years, 143 days, 7 hours, 38 minutes and 1 seconds
