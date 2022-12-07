# -*- coding: utf-8 -*-
import unittest

from constants import *
from gilded_rose import ItemFactory, GildedRose


class ConjuredItemTest(unittest.TestCase):
    def test_decreases_twice_as_fast(self):
        items = [ItemFactory.create(CONJURED, 10, 6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        print(items[0])
        self.assertEquals(4, items[0].quality)
        
    
if __name__ == '__main__':
    unittest.main()