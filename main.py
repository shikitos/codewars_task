# https://www.codewars.com/kata/52742f58faf5485cae000b9a/train/python
def format_duration(seconds):
    result = ''
    result_year = ''
    result_day = ''
    result_hour = ''
    result_minute = ''
    result_second = ''
    year = 24 * 3600 * 365 # 31536000
    day = 24 * 3600 # 86400
    hour = 60 * 60 # 3600
    minute = 60 # 60
    remainder_year = seconds - seconds % year
    remainder_day = seconds - seconds % day
    remainder_hour = seconds - seconds % hour
    remainder_minute = seconds - seconds % minute
    remainder_second = seconds
    calculation_flag = False
    last_item_flag = False
    list_items = [
        0, 0, 0, 0, 0
    ]
    separation_items = ['', '', '', '', '']
    current_item = 0
    prev_item = 0
    # TODO : two iterations: at the first we get the right format (without commas and "and"), the second: add separations syntax (we can understand using arrays)
    # TODO : Remake script using reminders
    i = 0
    while i < 2:
        # years
        if seconds >= year:
            if not calculation_flag:
                remainder_year = seconds - (seconds - seconds % year)
                result_year += f'{int(seconds / year)} year{"s" if seconds / year >= 2 else ""}'
                print(remainder_year)
                list_items[0] = 1
                # print(f"Total time: {seconds}. At the end of the year part, left time (2 years): {remainder_year}. \nRemainder: {remainder}. Remainder should be: {143 * day + 7 * hour + 38 * minute + 1}")
            # else:
            #     print("YEAR")
        # days
        if seconds >= day:
            print(seconds / day)
            if not calculation_flag:
                remainder = seconds - remainder_day
                result_day += f'{int(seconds / day) - int(seconds / year) * 365} day{"s" if seconds / day >= 2 else ""}'
                # print(f"Total time: {seconds}. At the end of the year part, left time: {remainder_day}. \nRemainder: {remainder}. Remainder should be: {143*day+7*hour+38*minute+1}") # should be 86400
                list_items[1] = 1
            # else:
            #     print("DAY")
        # hours
        if seconds >= hour:
            if not calculation_flag:
                remainder = seconds - remainder_hour
                result_hour += f'{int(seconds % day / hour)} hour{"s" if seconds % day / hour > 1 else ""}'
                # print(f"Total time: {seconds}. At the end of the year part, left time: {remainder_hour}. \nRemainder: {remainder}. Remainder should be: {143*day+7*hour+38*minute+1}")
                list_items[2] = 1
            # else:
            #     print("HOUR")
        # minutes
        if seconds % hour / 60 >= 1:
            if not calculation_flag:
                remainder = seconds - remainder_minute
                result_minute += f'{int(seconds % hour / 60)} minute{"s" if seconds % hour / 60 >= 2 else ""}'
                # print(f"Total time: {seconds}. At the end of the year part, left time: {remainder_minute}. \nRemainder: {remainder}. Remainder should be: {143 * day + 7 * hour + 38 * minute + 1}")
                list_items[3] = 1
            # else:
            #     print("MINUTE")
        # seconds
        if seconds % hour % minute != 0:
            if not calculation_flag:
                remainder = seconds - remainder_second
                result_second += f'{int(seconds % hour % minute)} second{"s" if seconds % hour % minute > 1 else ""}'
                # print(f"Total time: {seconds}. At the end of the year part, left time: {remainder_second}. \nRemainder: {remainder}. Remainder should be: {143 * day + 7 * hour + 38 * minute + 1}")
                list_items[4] = 1
            # else:
            #     print("SECONDS")
        if calculation_flag:
            for i in range(len(list_items)):
                if list_items[i]:
                    print("REGULAR CHANGE ITEM NUMBER: " + str(i))
                    separation_items[i] = ', '
                if not list_items[i] and not last_item_flag and list_items.count(1) >= 2:
                    print("CHANGE ITEM NUMBER " + str(i - 1))
                    separation_items[i - 1] = ' and '
                    # print("HERE" + separation_items[i-1] + "HERE " + str(i))
                    last_item_flag = True
                if i == len(list_items) - 1 and list_items[i]:
                    print("MIDDLE THING")
                    separation_items[-i] = ' and '
                if last_item_flag:
                    separation_items[i] = ''
            print(list_items)
            print(separation_items)
        calculation_flag = True
        i += 1
    result = f"{result_year}{separation_items[4]}{result_day}{separation_items[3]}{result_hour}{separation_items[2]}{result_minute}{separation_items[1]}{result_second}"
    return f"@@@@@@ OUTPUT RESULT: {result}"


# print(format_duration(1))  # 1 second
print(format_duration(62))  # 1 minute and 2 seconds
print(format_duration(120))  # 2 minutes
print(format_duration(3600))  # 1 hour
print(format_duration(7264))  # 2 hours, 1 minute and 4 seconds
print(format_duration(90000))  # 1 day and 1 hour
print(format_duration(10509999))  # 121 days, 15 hours, 26 minutes and 39 seconds
print(format_duration(2*24 * 3600 * 365)) # years
print(format_duration(75454681))  # 2 years, 143 days, 7 hours, 38 minutes and 1 seconds
