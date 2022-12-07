# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class AgedBrieTest(unittest.TestCase):
    def test_normal_aging(self):
        items = [Item("Aged Brie", 1, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(1, items[0].quality)
        
    def test_normal_aging_after_0(self):
        items = [Item("Aged Brie", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(2, items[0].quality)

        
if __name__ == '__main__':
    unittest.main()