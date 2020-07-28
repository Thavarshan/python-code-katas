from src.katas.gilded_rose import gilded_rose
import unittest


class GildedRoseTest(unittest.TestCase):

    def test_it_updates_normal_items_before_sell_date(self):
        item = gilded_rose.GildedRose.of('normal', 10, 5)
        item.tick()

        self.assertEqual(9, item.quality())
        self.assertEqual(4, item.sell_in())
