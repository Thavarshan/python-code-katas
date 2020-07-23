from src.katas import roman_numerals
from unittest_data_provider import data_provider
import unittest


class RomanNumeralsTest(unittest.TestCase):

    def setUp(self):
        self.generator = roman_numerals.RomanNumerals()

    def checks():
        return [
            [1, 'I'],
            [2, 'II'],
            [3, 'III'],
            [4, 'IV'],
            [5, 'V'],
            [6, 'VI'],
            [7, 'VII'],
            [8, 'VIII'],
            [9, 'IX'],
            [10, 'X'],
            [40, 'XL'],
            [50, 'L'],
            [90, 'XC'],
            [100, 'C'],
            [400, 'CD'],
            [500, 'D'],
            [900, 'CM'],
            [1000, 'M'],
            [3999, 'MMMCMXCIX'],
        ]

    @data_provider(checks)
    def test_it_generates_roman_numerals(self, number, numeral):
        self.assertEqual(numeral, self.generator.generate(number))

    def test_it_cannot_generate_a_roman_numeral_for_less_than_1(self):
        self.assertFalse(self.generator.generate(0))

    def test_it_cannot_generate_a_roman_numeral_for_more_than_3999(self):
        self.assertFalse(self.generator.generate(4000))


if __name__ == '__main__':
    unittest.main()
