#!/usr/bin/env python3

import itertools


def take_lines(filehandle):
    try:
        lines = itertools.islice(filehandle, 4)
    except StopIteration:
        return None
    yield lines


def take_char(lines):
    for line in next(lines):
        try:
            c = itertools.islice(line, 3)
        except StopIteration:
            return None
        yield c


def parse_char(stringed_char):
    switcher = {
            '     |  |': 1,
            ' _ _| |_ ': 2,
            '   |_|  |': 4
            }
    return switcher.get(stringed_char, None)


def process(char):
    listed_char = list(char)
    flattened_char = [y for x in listed_char for y in x]
    stringed_char = ''.join(flattened_char).strip('\n')
    parsed_char = parse_char(stringed_char)
    return parsed_char


def char_recon(file):
    with open(file) as f:
        lines = take_lines(f)
        raw_char = take_char(lines)
        processed_char = process(raw_char)
        print(processed_char)
        lines = take_lines(f)
        raw_char = take_char(lines)
        processed_char = process(raw_char)
        print(processed_char)


if __name__ == '__main__':
    char_recon('test.txt')
