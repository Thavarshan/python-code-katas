from src.katas import prime_factors
from unittest_data_provider import data_provider
import unittest


class PrimeFactorsTest(unittest.TestCase):

    def setUp(self):
        self.generator = prime_factors.PrimeFactors()

    def checks():
        return [
            [1, []],
            [2, [2]],
            [3, [3]],
            [4, [2, 2]],
            [5, [5]],
            [6, [2, 3]],
            [8, [2, 2, 2]],
            [9, [3, 3]],
            [100, [2, 2, 5, 5]]
        ]

    @data_provider(checks)
    def test_it_generates_prime_factors(self, number, factors):
        self.assertEqual(factors, self.generator.generate(number))


if __name__ == '__main__':
    unittest.main()
