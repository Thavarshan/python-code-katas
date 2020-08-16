from src.katas.unique_string_finder import UniqueStringFinder
from pprint import pprint
import unittest


class UniqueStringTest(unittest.TestCase):

    def test_it_finds_the_unique_string_from_list_of_strings(self):
        finder = UniqueStringFinder()

        self.assertEqual(
            finder.find_unique(['Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a']),
            'BbBb'
        )
        self.assertEqual(
            finder.find_unique(['abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba']),
            'foo'
        )
        self.assertEqual(finder.find_unique(['    ', 'a', '  ']), 'a')
