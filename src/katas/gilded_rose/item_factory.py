from abc import ABC, abstractmethod


class AbstractItem(ABC):
    quality = 0
    sell_in = 0

    def __init__(self, quality: int, sell_in: int):
        self.quality = quality
        self.sell_in = sell_in

    @abstractmethod
    def tick(self):
        pass


class Normal(AbstractItem):

    def tick(self):
        self.sell_in -= 1
        self.quality -= 1

        if self.sell_in <= 0:
            self.quality -= 1

        if self.quality < 0:
            self.quality = 0


class Brie(AbstractItem):

    def tick(self):
        self.sell_in -= 1
        self.quality += 1

        if self.sell_in <= 0:
            self.quality += 1

        if self.quality > 50:
            self.quality = 50


class Sulfuras(AbstractItem):

    def tick(self):
        return True


class BackstagePasses(AbstractItem):

    def tick(self):
        self.quality += 1

        if self.sell_in <= 10:
            self.quality += 1

        if self.sell_in <= 5:
            self.quality += 1

        if self.sell_in <= 0:
            self.quality = 0

        if self.quality > 50:
            self.quality = 50

        self.sell_in -= 1


class Conjured(AbstractItem):

    def tick(self):
        self.sell_in -= 1
        self.quality -= 2

        if self.sell_in <= 0:
            self.quality -= 2

        if self.quality < 0:
            self.quality = 0
