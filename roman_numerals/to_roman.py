#!/usr/bin/env python3

import sys


def first_digit(digit):
    first_digit = {
            0: '',
            1: 'I',
            2: 'II',
            3: 'III',
            4: 'IV',
            5: 'V',
            6: 'VI',
            7: 'VII',
            8: 'VIII',
            9: 'IX'
            }
    first, modulo = divmod(digit, 1)
    return first_digit.get(first), modulo


def second_digit(digit):
    second_digit = {
            0: '',
            1: 'X',
            2: 'XX',
            3: 'XXX',
            4: 'XL',
            5: 'L',
            6: 'LX',
            7: 'LXX',
            8: 'LXXX',
            9: 'XC'
            }
    second, modulo = divmod(digit, 10)
    return second_digit.get(second), modulo


def third_digit(digit):
    third_digit = {
            0: '',
            1: 'C',
            2: 'CC',
            3: 'CCC',
            4: 'CD',
            5: 'D',
            6: 'DC',
            7: 'DCC',
            8: 'DCCC',
            9: 'CM'
            }
    third, modulo = divmod(digit, 100)
    return third_digit.get(third), modulo


def fourth_digit(digit):
    fourth_digit = {
            0: '',
            1: 'M',
            2: 'MM',
            3: 'MMM'
            }
    fourth, modulo = divmod(digit, 1000)
    return fourth_digit.get(fourth), modulo


def parse_input(args):
    try:
        return int(args[1])
    except (ValueError, IndexError):
        print("please provide an integer as sole parameter")
        sys.exit(1)


def decimal_to_roman(decimal):
    decimal = parse_input(decimal)
    fourth, remaining = fourth_digit(decimal)
    third, remaining = third_digit(remaining)
    second, remaining = second_digit(remaining)
    first, remaining = first_digit(remaining)
    return str(fourth + third + second + first)


if __name__ == '__main__':
    print(decimal_to_roman(sys.argv))
