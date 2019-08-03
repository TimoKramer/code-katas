#!/usr/bin/env python3

import itertools

def take_lines(filehandle):
    return itertools.islice(filehandle, 4)

def take_char(lines):
    for line in lines:
        yield itertools.islice(line, 3)

def parse_char(stringed_char):
    switcher = {
            '     |  |': 1,
            ' _  _||_ ': 2
            }
    return switcher.get(stringed_char, None)

def process(char):
    flattened_char = [y for x in char for y in x]
    stringed_char = ''.join(flattened_char).strip('\n')
    parsed_char = parse_char(stringed_char)
    print(parsed_char)

def char_recon(file):
    with open(file) as f:
        lines = take_lines(f)
        raw_char = take_char(lines)
        processed_char = process(raw_char)

if __name__ == '__main__':
    char_recon('test.txt')
