import os
from datetime import datetime


def get_day_added(__date, __increament):
    even_months = [4, 6, 9, 11]
    odd_months = [1, 3, 5, 7, 8, 10, 12]
    exception_month = [2]
    if __date.day + __increament > 28 and __date.month in exception_month:
        if __date.year % 4 != 0:
            month = __date.month + 1
            day = __date.day + __increament - 28
        else:
            if __date.day + __increament == 29:
                month = __date.month
                day = 29
            else:
                month = __date.month + 1
                day = __date.day + __increament - 29
    elif __date.day + __increament > 30 and __date.month in even_months:
        month = __date.month + 1
        day = __date.day + __increament - 30
    elif __date.day + __increament > 31 and __date.month in odd_months:
        month = __date.month + 1
        day = __date.day + __increament - 31
    else:
        month = __date.month
        day = __date.day + __increament
    return __date.replace(month=month, day=day)


BASE_URL = os.getenv("WEB_URL", "https://www.makemytrip.com/")
MAX_WAIT_TIME = 45
USER = os.getenv("USER_NAME", "tesla.test.162@gmail.com")
PWD = os.getenv("USER_PASS", "4rA*X4rsW$6HAT6")
SCROLL_VIEWPORT_WAIT = 2

# USER INFO
F_NAME = os.getenv("FNAME", "Tesla")
L_NAME = os.getenv("LNAME", "Tester")
CONTACT = os.getenv("CONTACT", "9876543210")
LOCATION = os.getenv('LOCATION',"Bangkok")

_now = datetime.now()
_now = get_day_added(_now, 2)
format_ = "%a %b %d %Y"
IN_DAY = _now.strftime(format_)
_now = get_day_added(_now, 1)
OUT_DAY = _now.strftime(format_)

