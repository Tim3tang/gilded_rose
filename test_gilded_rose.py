# -*- coding: utf-8 -*-
import unittest
import pytest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_update_quality_for_normal_items(self):
        items = [Item("foo", 1, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(items[0].quality, 0)

    def test_update_quality_stops_at_0(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(items[0].quality, 0)

    def test_lowers_sell_in_for_normal_items(self):
        items = [Item("foo", 1, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(items[0].sell_in, 0)

    def test_lowers_sell_in_twice_if_overdue(self):
        items = [Item("foo", -1, 2)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(items[0].quality, 0)

    def test_quality_caps_at_50(self):
        items = [Item("Aged Brie", -25, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(items[0].quality, 50)

    def test_increase_quality_of_aged_brie(self):
        items = [Item("Aged Brie", -1, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(items[0].quality, 3)

    def test_quality_of_sulfuras_unchanged(self):
        items = [Item("Sulfuras, Hand of Ragnaros",0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(items[0].quality, 10)

    def test_backstage_pass_10_days(self):
         items = [Item("Backstage passes to a TAFKAL80ETC concert",10, 1)]
         gilded_rose = GildedRose(items)
         gilded_rose.update_quality()
         self.assertEquals(items[0].quality, 3)

    def test_backstage_pass_5_days(self):
         items = [Item("Backstage passes to a TAFKAL80ETC concert",5, 1)]
         gilded_rose = GildedRose(items)
         gilded_rose.update_quality()
         self.assertEquals(items[0].quality, 4)

    def test_backstage_pass_0_days(self):
         items = [Item("Backstage passes to a TAFKAL80ETC concert",0, 5)]
         gilded_rose = GildedRose(items)
         gilded_rose.update_quality()
         self.assertEquals(items[0].quality, 0)

    def test_conjured_items_quality_reduction(self):
         Conjured = "Conjured_item"
         items = [Item(Conjured,1, 2)]
         gilded_rose = GildedRose(items)
         gilded_rose.update_quality()
         self.assertEquals(items[0].quality, 0)

if __name__ == '__main__':
    unittest.main()
