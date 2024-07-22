


# Find day of given date

import calendar
MM,DD,YYYY=map(int,input().split())


print(calendar.day_name[calendar.weekday(YYYY,MM,DD)].upper())  # weekday method take year,month and date and then return day number , and by using day_name we can get name of day
