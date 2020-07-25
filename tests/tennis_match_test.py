from src.katas.tennis import tennis_match
from unittest_data_provider import data_provider
import unittest


class TennisMatchTest(unittest.TestCase):

    def scores():
        return [
            [0, 0, 'love-love'],
            [1, 0, 'fifteen-love'],
            [1, 1, 'fifteen-fifteen'],
            [2, 0, 'thirty-love'],
            [3, 0, 'forty-love'],
            [2, 2, 'thirty-thirty'],
            [3, 3, 'deuce'],
            [4, 4, 'deuce'],
            [5, 5, 'deuce'],
            [4, 3, 'Advantage: John'],
            [3, 4, 'Advantage: Jane'],
            [4, 0, 'Winner: John'],
            [0, 4, 'Winner: Jane'],
        ]

    @data_provider(scores)
    def test_it_generates_prime_factors(self, player_one, player_two, score):
        john = tennis_match.Player('John')
        jane = tennis_match.Player('Jane')
        game = tennis_match.Game(john, jane)

        index1 = 0
        while index1 < player_one:
            game.points_to(john.get_name())

            index1 += 1

        index2 = 0
        while index2 < player_two:
            game.points_to(jane.get_name())

            index2 += 1

        self.assertEqual(score, game.score())


if __name__ == '__main__':
    unittest.main()
