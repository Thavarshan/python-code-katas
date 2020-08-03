from src.katas import array_diff
import unittest


class ArrayDiffTest(unittest.TestCase):

    def test_it_removes_all_values_from_first_list_which_is_present_in_second_list(self):
        differentiator = array_diff.ArrayDiff()

        self.assertEqual([1, 3], differentiator.differentiate([1, 2, 2, 2, 3], [2]))
