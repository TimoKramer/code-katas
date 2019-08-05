#!/usr/bin/env python3

import sys


class ParsingError(Exception):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


def parse(char):
    char_code = ''.join(char)
    switcher = {
            ' _ | ||_|': '0',
            '     |  |': '1',
            ' _  _||_ ': '2',
            ' _  _| _|': '3',
            '   |_|  |': '4',
            ' _ |_  _|': '5',
            ' _ |_ |_|': '6',
            ' _   |  |': '7',
            ' _ |_||_|': '8',
            ' _ |_| _|': '9'
            }
    return switcher.get(char_code)


def loop(matrix):
    lines_of_chars = []
    for line_block in range(0, len(matrix), 3):
        chars = ''
        for char_block in range(0, len(matrix[0]), 3):
            char = []
            char.append(matrix[line_block][char_block])
            char.append(matrix[line_block][char_block + 1])
            char.append(matrix[line_block][char_block + 2])
            char.append(matrix[line_block + 1][char_block])
            char.append(matrix[line_block + 1][char_block + 1])
            char.append(matrix[line_block + 1][char_block + 2])
            char.append(matrix[line_block + 2][char_block])
            char.append(matrix[line_block + 2][char_block + 1])
            char.append(matrix[line_block + 2][char_block + 2])
            chars = chars + parse(char)
        lines_of_chars.append(chars)
    return lines_of_chars


def char_recon(filename):
    with open(filename) as f:
        matrix = f.readlines()
    matrix = [item.rstrip('\n') for item in matrix]
    matrix = [item for item in matrix if item]
    return loop(matrix)


def print_result(result):
    for i in result:
        print(i)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        print_result(char_recon(sys.argv[1]))
    else:
        print('this script expects the file to read as a string parameter')
