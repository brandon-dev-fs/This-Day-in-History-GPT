import datetime

def get_date():
    year = 0
    while not (year > 1850 and year < 2020):
        year = int(input("Enter a year (1851-2019): "))
    month = 0
    while not (month > 0 and month < 13):
        month = int(input("Enter a month (1-12): "))
    day = 0
    if month in [1,3,4,7,8,10,12]:
        while not (day > 0 and day < 32):
            day = int(input("Enter a day (1-31): "))
    elif month in [5,6,9,11]:
        while not (day > 0 and day < 31):
            day = int(input("Enter a day (1-30): "))
    else:
        if(year % 4 == 0 or year % 400 == 0):
            while not (day > 0 and day < 30):
                day = int(input("Enter a day (1-29): "))
        else:
            while not (day > 0 and day < 29):
                day = int(input("Enter a day (1-28): "))
    return datetime.datetime(year, month, day)

