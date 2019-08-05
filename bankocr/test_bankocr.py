#!/usr/bin/env python3

import unittest

import bankocr


class TestBankOCR(unittest.TestCase):

    def test_parse(self):
        self.assertIs(bankocr.parse([' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', '|']), 1)
        self.assertIs(bankocr.parse([' ', '_', ' ', '|', ' ', '|', '|', '_', '|']), 0)

    def test_loop(self):
        test_list = ['    _  _     _  _  _  _  _ ',
                     '  | _| _||_||_ |_   ||_||_|',
                     '  ||_  _|  | _||_|  ||_| _|']
        self.assertEqual(bankocr.loop(test_list), [[1, 2, 3, 4, 5, 6, 7, 8, 9]])

    def test_char_recon(self):
        self.assertEqual(bankocr.char_recon('test.txt'), [[1, 2, 3, 4, 5, 6, 7, 8, 9], [4, 9, 0, 0, 6, 7, 7, 1, 5]])


if __name__ == '__main__':
    unittest.main()
