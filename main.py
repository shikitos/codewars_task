# https://www.codewars.com/kata/52742f58faf5485cae000b9a/train/python
def format_duration(seconds):
    list_of_durations = {
        "minute": 60,
        "hour": 60 * 60,
        "day": 24 * 3600,
        "year": 24 * 3600 * 365
    }
    result = ''
    year = list_of_durations["year"]
    day = list_of_durations["day"]
    hour = list_of_durations["hour"]
    minute = list_of_durations["minute"]

    # years
    if seconds >= year:
        result += f'{int(seconds / year)} year{"s" if seconds / year >= 2 else ""}'
        remainder = seconds - int(seconds / year) * year
        print(int(seconds / year) * year)
        print(remainder)
    # days
    if seconds >= day:
        result += f'{int(seconds / day) - int(seconds / year) * 365} day{"s" if seconds / day >= 2 else ""}'
    # hours
    if seconds >= list_of_durations['hour']:
        result += f'{int(seconds % day / hour)} hour{"s" if seconds / hour > 1 else ""}'
    # minutes
    if seconds % hour / 60 >= 1:
        result += f'{int(seconds % hour / 60)} minute{"s" if seconds % hour / 60 >= 2 else ""}'
    # seconds
    if seconds % hour % minute != 0:
        result += f'{int(seconds % hour % minute)} second{"s" if seconds % hour % minute > 1 else ""}'
    return result


print(format_duration(1))  # 1 second
print(format_duration(62))  # 1 minute and 2 seconds
print(format_duration(120))  # 2 minutes
print(format_duration(3600))  # 1 hour
print(format_duration(7264))  # 2 hours, 1 minute and 4 seconds
print(format_duration(90000))  # 1 day and 1 hour
print(format_duration(10509999))  # 121 days, 15 hours, 26 minutes and 39 seconds
print(format_duration(75454681))  # 2 years, 143 days, 7 hours, 38 minutes and 1 seconds
