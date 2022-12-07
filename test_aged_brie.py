# -*- coding: utf-8 -*-
import unittest

from constants import *
from gilded_rose import ItemFactory, GildedRose


class AgedBrieTest(unittest.TestCase):
    def test_normal_aging(self):
        items = [ItemFactory.create(AGED_BRIE, 1, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        print(items[0])
        self.assertEquals(1, items[0].quality)
        
    def test_normal_aging_after_0(self):
        items = [ItemFactory.create(AGED_BRIE, 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(2, items[0].quality)

if __name__ == '__main__':
    unittest.main()