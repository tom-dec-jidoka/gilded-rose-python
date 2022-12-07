# -*- coding: utf-8 -*-
import unittest

from constants import *
from gilded_rose import ItemFactory, GildedRose


class AgedBrieTest(unittest.TestCase):
    def test_quility_max_brie(self):
        items = [ItemFactory.create(AGED_BRIE, 1, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(50, items[0].quality)

    def test_quality_max_backstage_passes_12(self):
        items = [ItemFactory.create(BACKSTAGE_PASS, 12, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(50, items[0].quality)  
          
    def test_quality_max_backstage_passes_10(self):
        items = [ItemFactory.create(BACKSTAGE_PASS, 10, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(50, items[0].quality)  
    
    def test_quality_max_backstage_passes_5(self):
        items = [ItemFactory.create(BACKSTAGE_PASS, 5, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(50, items[0].quality)     
           
if __name__ == '__main__':
    unittest.main()