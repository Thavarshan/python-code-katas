from src.katas.gilded_rose import gilded_rose
import unittest


class GildedRoseTest(unittest.TestCase):

    def test_it_updates_normal_items_before_the_sell_date(self):
        shop = gilded_rose.GildedRose()
        item = shop.of('normal', 10, 5)
        item.tick()

        self.assertEqual(9, item.quality)
        self.assertEqual(4, item.sell_in)

    def test_it_updates_normal_items_on_the_sell_date(self):
        shop = gilded_rose.GildedRose()
        item = shop.of('normal', 10, 0)
        item.tick()

        self.assertEqual(8, item.quality)
        self.assertEqual(-1, item.sell_in)

    def test_it_updates_normal_items_after_the_sell_date(self):
        shop = gilded_rose.GildedRose()
        item = shop.of('normal', 10, -5)
        item.tick()

        self.assertEqual(8, item.quality)
        self.assertEqual(-6, item.sell_in)

    def test_it_updates_normal_items_with_a_quality_of_zero(self):
        shop = gilded_rose.GildedRose()
        item = shop.of('normal', 0, 5)
        item.tick()

        self.assertEqual(0, item.quality)
        self.assertEqual(4, item.sell_in)

    def test_it_updates_brie_items_before_the_sell_date(self):
        shop = gilded_rose.GildedRose()
        item = shop.of('Aged Brie', 10, 5)
        item.tick()

        self.assertEqual(11, item.quality)
        self.assertEqual(4, item.sell_in)

    def test_it_updates_brie_items_before_the_sell_date_with_maximum_quality(self):
        shop = gilded_rose.GildedRose()
        item = shop.of('Aged Brie', 50, 5)
        item.tick()

        self.assertEqual(50, item.quality)
        self.assertEqual(4, item.sell_in)

    def test_it_updates_brie_items_on_the_sell_date(self):
        shop = gilded_rose.GildedRose()
        item = shop.of('Aged Brie', 10, 0)
        item.tick()

        self.assertEqual(12, item.quality)
        self.assertEqual(-1, item.sell_in)

    def test_it_updates_brie_items_on_the_sell_date_near_maximum_quality(self):
        shop = gilded_rose.GildedRose()
        item = shop.of('Aged Brie', 49, 0)
        item.tick()

        self.assertEqual(50, item.quality)
        self.assertEqual(-1, item.sell_in)

    def test_it_updates_brie_items_on_the_sell_date_with_maximum_quality(self):
        shop = gilded_rose.GildedRose()
        item = shop.of('Aged Brie', 50, 0)
        item.tick()

        self.assertEqual(50, item.quality)
        self.assertEqual(-1, item.sell_in)

    def test_it_updates_brie_items_after_the_sell_date(self):
        shop = gilded_rose.GildedRose()
        item = shop.of('Aged Brie', 10, -10)
        item.tick()

        self.assertEqual(12, item.quality)
        self.assertEqual(-11, item.sell_in)

    def test_it_updates_brie_items_after_the_sell_date_with_maximum_quality(self):
        shop = gilded_rose.GildedRose()
        item = shop.of('Aged Brie', 50, -10)
        item.tick()

        self.assertEqual(50, item.quality)
        self.assertEqual(-11, item.sell_in)

    def test_it_updates_sulfuras_items_before_the_sell_date(self):
        shop = gilded_rose.GildedRose()
        item = shop.of('Sulfuras, Hand of Ragnaros', 10, 5)
        item.tick()

        self.assertEqual(10, item.quality)
        self.assertEqual(5, item.sell_in)

    def test_it_updates_sulfuras_items_on_the_sell_date(self):
        shop = gilded_rose.GildedRose()
        item = shop.of('Sulfuras, Hand of Ragnaros', 10, 5)
        item.tick()

        self.assertEqual(10, item.quality)
        self.assertEqual(5, item.sell_in)

    def test_it_updates_sulfuras_items_after_the_sell_date(self):
        shop = gilded_rose.GildedRose()
        item = shop.of('Sulfuras, Hand of Ragnaros', 10, -1)
        item.tick()

        self.assertEqual(10, item.quality)
        self.assertEqual(-1, item.sell_in)

    def test_it_updates_backstage_pass_items_long_before_the_sell_date(self):
        shop = gilded_rose.GildedRose()
        item = shop.of(
            'Backstage passes to a TAFKAL80ETC concert',
            10,
            11
        )
        item.tick()

        self.assertEqual(11, item.quality)
        self.assertEqual(10, item.sell_in)

    def test_it_updates_backstage_pass_items_close_to_the_sell_date(self):
        shop = gilded_rose.GildedRose()
        item = shop.of(
            'Backstage passes to a TAFKAL80ETC concert',
            10,
            10
        )
        item.tick()

        self.assertEqual(12, item.quality)
        self.assertEqual(9, item.sell_in)

    def test_it_updates_backstage_pass_items_close_to_the_sell_data_at_max_quality(self):
        shop = gilded_rose.GildedRose()
        item = shop.of(
            'Backstage passes to a TAFKAL80ETC concert',
            50,
            10
        )
        item.tick()

        self.assertEqual(50, item.quality)
        self.assertEqual(9, item.sell_in)

    def test_it_updates_backstage_pass_items_very_close_to_the_sell_date(self):
        shop = gilded_rose.GildedRose()
        item = shop.of(
            'Backstage passes to a TAFKAL80ETC concert',
            10,
            5
        )
        item.tick()

        self.assertEqual(13, item.quality)
        self.assertEqual(4, item.sell_in)

    def test_it_updates_backstage_pass_items_very_close_to_the_sell_date_at_max_quality(self):
        shop = gilded_rose.GildedRose()
        item = shop.of(
            'Backstage passes to a TAFKAL80ETC concert',
            50,
            5
        )
        item.tick()

        self.assertEqual(50, item.quality)
        self.assertEqual(4, item.sell_in)

    def test_it_updates_backstage_pass_items_with_one_day_left_to_sell(self):
        shop = gilded_rose.GildedRose()
        item = shop.of(
            'Backstage passes to a TAFKAL80ETC concert',
            10,
            1
        )
        item.tick()

        self.assertEqual(13, item.quality)
        self.assertEqual(0, item.sell_in)

    def test_it_updates_backstage_pass_items_with_one_day_left_to_sell_at_max_quality(self):
        shop = gilded_rose.GildedRose()
        item = shop.of(
            'Backstage passes to a TAFKAL80ETC concert',
            50,
            1
        )
        item.tick()

        self.assertEqual(50, item.quality)
        self.assertEqual(0, item.sell_in)

    def test_it_updates_backstage_pass_items_on_the_sell_date(self):
        shop = gilded_rose.GildedRose()
        item = shop.of(
            'Backstage passes to a TAFKAL80ETC concert',
            10,
            0
        )
        item.tick()

        self.assertEqual(0, item.quality)
        self.assertEqual(-1, item.sell_in)

    def test_it_updates_backstage_pass_items_after_the_sell_date(self):
        shop = gilded_rose.GildedRose()
        item = shop.of(
            'Backstage passes to a TAFKAL80ETC concert',
            10,
            -1
        )
        item.tick()

        self.assertEqual(0, item.quality)
        self.assertEqual(-2, item.sell_in)

    def test_it_updates_conjured_items_before_the_sell_date(self):
        shop = gilded_rose.GildedRose()
        item = shop.of('Conjured Juna Cake', 10, 10)
        item.tick()

        self.assertEqual(8, item.quality)
        self.assertEqual(9, item.sell_in)

    def test_it_updates_conjured_items_at_zero_quality(self):
        shop = gilded_rose.GildedRose()
        item = shop.of('Conjured Juna Cake', 0, 10)
        item.tick()

        self.assertEqual(0, item.quality)
        self.assertEqual(9, item.sell_in)

    def test_it_updates_conjured_items_on_the_sell_date(self):
        shop = gilded_rose.GildedRose()
        item = shop.of('Conjured Juna Cake', 10, 0)
        item.tick()

        self.assertEqual(6, item.quality)
        self.assertEqual(-1, item.sell_in)

    def test_it_updates_conjured_items_on_the_sell_date_at_0_quality(self):
        shop = gilded_rose.GildedRose()
        item = shop.of('Conjured Juna Cake', 0, 0)
        item.tick()

        self.assertEqual(0, item.quality)
        self.assertEqual(-1, item.sell_in)

    def test_it_updates_conjured_items_after_the_sell_date(self):
        shop = gilded_rose.GildedRose()
        item = shop.of('Conjured Juna Cake', 10, -10)
        item.tick()

        self.assertEqual(6, item.quality)
        self.assertEqual(-11, item.sell_in)

    def test_it_updates_conjured_items_after_the_sell_date_at_zero_quality(self):
        shop = gilded_rose.GildedRose()
        item = shop.of('Conjured Juna Cake', 0, -10)
        item.tick()

        self.assertEqual(0, item.quality)
        self.assertEqual(-11, item.sell_in)
