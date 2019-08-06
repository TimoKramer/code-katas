#!/usr/bin/env python3

import sys
import calendar


def cal(month, year, firstweekday=6):
    try:
        month = int(month)
        year = int(year)
    except ValueError:
        return 'expecting integer parameters as input'
    cal = calendar.TextCalendar(firstweekday)
    return cal.formatmonth(int(year), int(month))


def print_result(result):
    print(result)


if __name__ == '__main__':
    if len(sys.argv) == 3:
        print_result(cal(sys.argv[1], sys.argv[2]))
    else:
        print('this script expects two integer parameters:')
        print('\t- the month to print as number from 1 to 12')
        print('\t- the year which month to print of')
