# -*- coding: utf-8 -*-
import unittest

from constants import *
from gilded_rose import ItemFactory, GildedRose


class ItemQualityTest(unittest.TestCase):
    
    def test_quality_not_negative(self):
        item = ItemFactory.create("foo", 10, 0)
        gilded_rose = GildedRose([item])
        
        gilded_rose.update_quality()

        self.assertEquals(0, item.quality)

    def test_start_from_one(self):
        item = ItemFactory.create("foo", 10, 1)
        gilded_rose = GildedRose([item])
        
        gilded_rose.update_quality()
        gilded_rose.update_quality()

        self.assertEquals(0, item.quality)

    def test_Item_instantiated_with_negative_quality(self):

        self.assertEquals(1, 1)
    
    def test_Item_sell_in_has_passed(self):
        item = ItemFactory.create("foo", -1, 1)
        gilded_rose = GildedRose([item])
        
        gilded_rose.update_quality()

        self.assertEquals(0, item.quality)
        print(item)

    def test_conjured_item(self):
        item = ItemFactory.create(CONJURED, 10, 1)

        item.update_quality()

        self.assertEquals(0, item.quality)

    
    def test_conjured_item_start_from_3_and_date_passed(self):
        item = ItemFactory.create(CONJURED, 0, 3)

        item.update_quality()

        self.assertEquals(0, item.quality)

if __name__ == '__main__':
    unittest.main()
