#!/usr/bin/env python3

import itertools

def take_lines(number, filehandle):
    return itertools.islice(filehandle, number)

def take_char(char_length, lines):
    for line in lines:
        yield itertools.islice(line, char_length)

def char_recon(file):
    with open(file) as f:
        lines = take_lines(4, f)
        char = take_char(3, lines)
        for i in char:
            print(list(i))

if __name__ == '__main__':
    char_recon('test.txt')
