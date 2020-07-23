from src.katas import string_calculator
from src.katas.exceptions.illegal_argument_error import IllegalArgumentError
import unittest


class StringCalculatorTest(unittest.TestCase):

    def test_it_evaluates_an_empty_string_to_0(self):
        calculator = string_calculator.StringCalculator()

        self.assertEqual(0, calculator.add(''))

    def test_it_finds_the_sum_of_a_single_number(self):
        calculator = string_calculator.StringCalculator()

        self.assertEqual(5, calculator.add('5'))

    def test_it_finds_the_sum_of_two_number(self):
        calculator = string_calculator.StringCalculator()

        self.assertEqual(10, calculator.add('5, 5'))

    def test_it_finds_the_sum_of_any_amount_of_numbers(self):
        calculator = string_calculator.StringCalculator()

        self.assertEqual(19, calculator.add('5, 5, 5, 4'))

    def test_it_accepts_a_new_line_character_as_a_delimeter_too(self):
        calculator = string_calculator.StringCalculator()

        self.assertEqual(10, calculator.add("5\n5"))

    def test_negative_numbers_are_not_allowed(self):
        calculator = string_calculator.StringCalculator()

        with self.assertRaises(IllegalArgumentError):
            calculator.add('5, -4')

    def test_numbers_bigger_than_1000_are_ignored(self):
        calculator = string_calculator.StringCalculator()

        self.assertEqual(5, calculator.add('5, 1001'))
