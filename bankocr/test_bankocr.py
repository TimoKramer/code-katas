#!/usr/bin/env python3

import unittest

import bankocr


class TestBankOCR(unittest.TestCase):

    def test_parse(self):
        self.assertIs(bankocr.parse([' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', '|']), '1')
        self.assertIs(bankocr.parse([' ', '_', ' ', '|', ' ', '|', '|', '_', '|']), '0')

    def test_loop(self):
        test_list = ['    _  _     _  _  _  _  _ ',
                     '  | _| _||_||_ |_   ||_||_|',
                     '  ||_  _|  | _||_|  ||_| _|']
        self.assertEqual(bankocr.loop(test_list), ['123456789'])

    def test_loop_failing(self):
        test_list = ['  _ _  _     _  _  _  _  _ ',
                     '  _ _| _||_||_ |_   ||_||_|',
                     '  _|_  _|  | _||_|  ||_| _|']
        self.assertEqual(bankocr.loop(test_list), ['Fehlerhafte Zeile'])

    def test_char_recon(self):
        self.assertEqual(bankocr.char_recon('test.txt'), ['123456789', '490067715'])


if __name__ == '__main__':
    unittest.main()
