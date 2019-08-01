#!/usr/bin/env python3

import unittest
import itertools

import bankocr


class TestBankOCR(unittest.TestCase):

    def test_take_lines_instance(self):
        self.assertIsInstance(bankocr.take_lines(3, 'test.txt'), itertools.islice)

    def test_take_4_lines(self):
        self.assertEqual(len(list(bankocr.take_lines(4, 'test.txt'))), 4)

if __name__ == '__main__':
    unittest.main()
