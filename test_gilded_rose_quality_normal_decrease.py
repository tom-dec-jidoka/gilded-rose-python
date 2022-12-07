# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseQualityDecreasesTwiceAsFastTest(unittest.TestCase):
    def test_normal_decrease(self):
        items = [Item("Dummy", 2, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(1, items[0].sell_in)
        self.assertEquals(9, items[0].quality)
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].sell_in)
        self.assertEquals(8, items[0].quality)
        

    def test_two_decrease(self):
        items = [Item("Dummy", 2, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        self.assertEquals(-1, items[0].sell_in)
        self.assertEquals(6, items[0].quality)

        
if __name__ == '__main__':
    unittest.main()
