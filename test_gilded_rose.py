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

if __name__ == '__main__':
    unittest.main()
