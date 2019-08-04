#!/usr/bin/env python3

def char_recon(filename):
    matrix = open(filename).readlines()
    matrix = [item.rstrip('\n') for item in matrix]
    chars = []
    for line_block in range(0, len(matrix), 4):
        print('line_block ' + str(line_block))
        for char_block in range(0, len(matrix[0]), 3):
            print('char_block ' + str(char_block))
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
            chars.append(char)

if __name__ == '__main__':
    char_recon('test.txt')
