# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

SULFURAS_NAME = "Sulfuras, Hand of Ragnaros"

class SulfurasIsNeverSoldTest(unittest.TestCase):
    def test_start_on_100(self):
        item = Item(SULFURAS_NAME, 100, 100)
        gilded_rose = GildedRose([item])
        
        gilded_rose.update_quality()
        
        self.assertEquals(100, item.sell_in)

    def test_start_on_0(self):
        item = Item(SULFURAS_NAME, 0, 100)
        gilded_rose = GildedRose([item])
        
        gilded_rose.update_quality()
        
        self.assertEquals(0, item.sell_in)
        
    def test_start_on_negative_100(self):
        item = Item(SULFURAS_NAME, -100, 100)
        gilded_rose = GildedRose([item])
        
        gilded_rose.update_quality()
        
        self.assertEquals(-100, item.sell_in)
    
class SulfurasDoesNotDecreaseInQuality(unittest.TestCase):
    def test_start_on_100(self):
        item = Item(SULFURAS_NAME, 100, 100)
        gilded_rose = GildedRose([item])
        
        gilded_rose.update_quality()
        
        self.assertEquals(100, item.quality)

    def test_start_on_0(self):
        item = Item(SULFURAS_NAME, 100, 0)
        gilded_rose = GildedRose([item])
        
        gilded_rose.update_quality()
        
        self.assertEquals(0, item.quality)

    def test_start_on_negative_100(self):
        item = Item(SULFURAS_NAME, 100, -100)
        gilded_rose = GildedRose([item])
        
        gilded_rose.update_quality()
        
        self.assertEquals(-100, item.quality)


if __name__ == '__main__':
    unittest.main()
