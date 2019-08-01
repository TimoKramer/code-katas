#!/usr/bin/env python3

import itertools

def take_lines(number, filehandle):
    return itertools.islice(filehandle, number)

def char_recon(file):
    with open(file) as f:
        print(list(take_lines(4, f)))

if __name__ == '__main__':
    char_recon('test.txt')
