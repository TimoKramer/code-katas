#!/usr/bin/env python3

import sys
import calendar
import datetime


def cal(month, year, firstweekday=6):
    cal = calendar.TextCalendar(firstweekday)
    try:
        return cal.formatmonth(int(year), int(month))
    except IndexError:
        sys.exit(print_help())


def parse_weekday(weekday):
    weekday = str(weekday)
    weekdays = {
            'montag': 0,
            'dienstag': 1,
            'mittwoch': 2,
            'donnerstag': 3,
            'freitag': 4,
            'samstag': 5,
            'sonntag': 6
            }
    return weekdays.get(weekday.lower())


def get_current_month():
    return datetime.date.today().month


def get_current_year():
    return datetime.date.today().year


def parse_input(month, year, weekday):
    try:
        month = int(month)
        year = int(year)
        weekday = int(parse_weekday(weekday))
    except ValueError:
        sys.exit(print_help())
    except TypeError:
        sys.exit(print_help())
    return month, year, weekday


def print_result(result):
    print(result)
    return


def print_help():
    print('\nThis script accepts three optional positional parameters:')
    print('\t1. the month to print as integer from 1 to 12')
    print('\t2. the year which month to print of as integer')
    print('\t3. the weekday to start the week with as string\n')
    print('This script does either accept month and year,')
    print('or month, year and weekday, or only weekday or nothing.\n')
    print('But it does not accept only one of month and year.')


def myargparse(myargs):
    if len(myargs) == 2 and myargs[1] == 'help':
        print_help()
    elif len(myargs) == 1:
        month, year, weekday = parse_input(get_current_month(), get_current_year(), 'Sonntag')
        print_result(cal(month, year, weekday))
    elif len(myargs) == 2:
        month, year, weekday = parse_input(get_current_month(), get_current_year(), myargs[1])
        print_result(cal(month, year, weekday))
    elif len(myargs) == 3:
        month, year, weekday = parse_input(myargs[1], 'Sonntag')
        print_result(cal(month, year, weekday))
    elif len(myargs) == 4:
        month, year, weekday = parse_input(myargs[1], myargs[2], myargs[3])
        print_result(cal(month, year, weekday))
    else:
        print_help()


if __name__ == '__main__':
    myargparse(sys.argv)
