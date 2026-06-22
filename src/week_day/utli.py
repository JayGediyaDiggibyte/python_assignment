import calendar

def find_day(month, day, year):
    day_index = calendar.weekday(year, month, day)
    return calendar.day_name[day_index].upper()