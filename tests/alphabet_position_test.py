from src.katas import alphabet_position
import unittest


class AlphabetPositionTest(unittest.TestCase):

    def test_replaces_all_alphabetic_characters_to_its_relevant_position_in_the_alphabet(self):
        finder = alphabet_position.AlphabetPosition()

        self.assertEqual(
            "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11",
            finder.find_position("The sunset sets at twelve o' clock.")
        )
