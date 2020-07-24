from src.katas import tennis_match
import unittest


class TennisMatchTest(unittest.TestCase):

    def test_basic(self):
        self.player = tennis_match.TennisMatch()
        self.assertIsInstance(self.player, tennis_match.TennisMatch)
