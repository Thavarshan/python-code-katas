class Player:
    __points = 0

    def __init__(self, name: str):
        self._name = name

    def score(self):
        self.__points += 1

    def get_points(self):
        return self.__points

    def get_name(self):
        return self._name


class Game:

    def __init__(self, player_one: Player, player_two: Player):
        self.player_one = player_one
        self.player_two = player_two

    def points_to(self, player_name: str):
        if self.player_one.get_name() == player_name:
            return self.player_one.score()

        if self.player_two.get_name() == player_name:
            return self.player_two.score()

    def score(self):
        if self._has_winner():
            return f'Winner: {self._leader()}'

        if self._has_advantage():
            return f'Advantage: {self._leader()}'

        if self._is_deuce():
            return 'deuce'

        player_one_points = self._points_to_term(self.player_one.get_points())
        player_two_points = self._points_to_term(self.player_two.get_points())

        return f'{player_one_points}-{player_two_points}'

    def _leader(self):
        if self.player_one.get_points() > self.player_two.get_points():
            return self.player_one.get_name()

        return self.player_two.get_name()

    def _has_winner(self):
        player_one_points = self.player_one.get_points()
        player_two_points = self.player_two.get_points()

        if player_one_points < 4 and player_two_points < 4:
            return False

        return abs(player_one_points - player_two_points) >= 2

    def _has_advantage(self):
        if not self._has_reached_deuce_threshold():
            return False

        return not self._is_deuce()

    def _is_deuce(self):
        if not self._has_reached_deuce_threshold():
            return False

        return self.player_one.get_points() == self.player_two.get_points()

    def _has_reached_deuce_threshold(self):
        player_one_points = self.player_one.get_points()
        player_two_points = self.player_two.get_points()

        return player_one_points >= 3 and player_two_points >= 3

    def _points_to_term(self, point: int):
        points = {
            0: 'love',
            1: 'fifteen',
            2: 'thirty',
            3: 'forty'
        }

        return points[point]
