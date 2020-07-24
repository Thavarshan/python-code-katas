from .exceptions.illegal_argument_error import IllegalArgumentError
import re


class StringCalculator:

    def add(self, numbers: str):
        if not numbers:
            return 0

        numbers = self.convert_to_integers(numbers)

        for number in numbers:
            self.is_negative_number(number)

        return sum(numbers)

    def convert_to_integers(self, string_list):
        numbers = list(map(int, re.split(',|\n', string_list)))

        return list(filter(lambda number: number <= 1000, numbers))

    def is_negative_number(self, number: int):
        if number < 0:
            raise IllegalArgumentError('Numbers cannot be negative.')
