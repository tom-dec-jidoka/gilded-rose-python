# -*- coding: utf-8 -*-
import unittest

from constants import *
from gilded_rose import Item, GildedRose


class GildedRoseQualityDecreasesTwiceAsFastTest(unittest.TestCase):
    def test_increase_if_more_than_10_days(self):
        items = [Item(BACKSTAGE_PASS, 12, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(11, items[0].sell_in)
        self.assertEquals(11, items[0].quality)
        gilded_rose.update_quality()
        self.assertEquals(10, items[0].sell_in)
        self.assertEquals(12, items[0].quality)

    def test_increase_two_if_less_than_10_days_but_more_than_5(self):
        items = [Item(BACKSTAGE_PASS, 8, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(7, items[0].sell_in)
        self.assertEquals(12, items[0].quality)
        gilded_rose.update_quality()
        self.assertEquals(6, items[0].sell_in)
        self.assertEquals(14, items[0].quality)

    def test_increase_tree_if_less_than_10_days_but_more_than_5(self):
        items = [Item(BACKSTAGE_PASS, 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(4, items[0].sell_in)
        self.assertEquals(13, items[0].quality)
        gilded_rose.update_quality()
        self.assertEquals(3, items[0].sell_in)
        self.assertEquals(16, items[0].quality)
        
    def test_worthless_if_concert_passed(self):
        items = [Item(BACKSTAGE_PASS, 2, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(1, items[0].sell_in)
        self.assertEquals(13, items[0].quality)
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].sell_in)
        self.assertEquals(16, items[0].quality)
        gilded_rose.update_quality()
        self.assertEquals(-1, items[0].sell_in)
        self.assertEquals(0, items[0].quality)

if __name__ == '__main__':
    unittest.main()
