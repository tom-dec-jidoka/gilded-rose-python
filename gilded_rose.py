# -*- coding: utf-8 -*-
from constants import *

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.update_quality()

class ItemFactory:
    def create(name, sell_in, quality):
        if(name == AGED_BRIE):
            return AgdBrie(name, sell_in, quality)
        else:
            return Item(name, sell_in, quality)
class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality
        if(name == AGED_BRIE):
            self = AgdBrie(name, sell_in, quality)
    
    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def update_quality(self):
        if self.name != AGED_BRIE and self.name != BACKSTAGE_PASS:
            if self.quality > 0:
                if self.name != SULFURAS:
                    self.quality = self.quality - 1
        else:
            if self.quality < 50:
                self.quality = self.quality + 1
                if self.name == BACKSTAGE_PASS:
                    if self.sell_in < 11:
                        if self.quality < 50:
                            self.quality = self.quality + 1
                    if self.sell_in < 6:
                        if self.quality < 50:
                            self.quality = self.quality + 1
        if self.name != SULFURAS:
            self.sell_in = self.sell_in - 1
        if self.sell_in < 0:
            if self.name != AGED_BRIE:
                if self.name != BACKSTAGE_PASS:
                    if self.quality > 0:
                        if self.name != SULFURAS:
                            self.quality = self.quality - 1
                else:
                    self.quality = self.quality - self.quality
            else:
                if self.quality < 50:
                    self.quality = self.quality + 1

class AgdBrie(Item):
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "Hi I am Brie %s, %s, %s" % (self.name, self.sell_in, self.quality)
