#!/usr/bin/env python3

import sys
import calendar


def cal(month, year, firstweekday=6):
    cal = calendar.TextCalendar(firstweekday)
    return cal.formatmonth(int(year), int(month))


def parse_input(month, year):
    try:
        month = int(month)
        year = int(year)
    except ValueError:
        raise
    return month, year


def print_result(result):
    print(result)


if __name__ == '__main__':
    if len(sys.argv) == 3:
        month, year = parse_input(sys.argv[1], sys.argv[2])
        print_result(cal(month, year))
    else:
        print('this script expects two integer parameters:')
        print('\t- the month to print as number from 1 to 12')
        print('\t- the year which month to print of')
