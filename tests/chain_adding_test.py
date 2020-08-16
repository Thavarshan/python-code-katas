from src.katas.chain_adding import Add
import unittest


class ChainAddingTest(unittest.TestCase):

    def test_it_adds_numbers_together_when_called_in_succession(self):
        self.assertEqual(3, Add(1)(2))
        self.assertEqual(6, Add(1)(2)(3))
        self.assertEqual(10, Add(1)(2)(3)(4))
