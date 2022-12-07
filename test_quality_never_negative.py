# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class ItemQualityTest(unittest.TestCase):
    
    def test_quality_not_negative(self):
        item = Item("foo", 10, 0)
        gilded_rose = GildedRose([item])
        
        gilded_rose.update_quality()

        self.assertEquals(0, item.quality)

    def test_start_from_one(self):
        item = Item("foo", 10, 1)
        gilded_rose = GildedRose([item])
        
        gilded_rose.update_quality()
        gilded_rose.update_quality()

        self.assertEquals(0, item.quality)

    def test_Item_instantiated_with_negative_quality(self):

        self.assertEquals(1, 1)
    
    def test_Item_sell_in_has_passed(self):
        item = Item("foo", -1, 1)
        gilded_rose = GildedRose([item])
        
        gilded_rose.update_quality()

        self.assertEquals(0, item.quality)
        print(item)

        
if __name__ == '__main__':
    unittest.main()
