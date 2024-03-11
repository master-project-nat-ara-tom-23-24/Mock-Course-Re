#!/usr/bin/env python3

from unittest import TestCase

from hotdog import bill

menu = {
  "Hot Dog":             4.50,
  "Spicy Dog":           5.00,
  "Vegan Dog":           4.50,
  "Water":               1.00,
  "Fizzy Drink":         3.50,
  "Beer":                5.00
}

class HotDogTest(TestCase):
    def test_empty(self):
        with self.assertRaises(ValueError):
            bill({}, menu)

    def test_everything(self):
        order = {
          "Hot Dog":             1,
          "Spicy Dog":           1,
          "Vegan Dog":           1,
          "Water":               1,
          "Fizzy Drink":         1,
          "Beer":                1
        }
        self.assertAlmostEqual(bill(order, menu), 22.5)

    def test_single(self):
        order = {"Hot Dog": 1}
        self.assertAlmostEqual(bill(order, menu), 4.50)

    def test_two(self):
        order = {"Hot Dog": 2}
        self.assertAlmostEqual(bill(order, menu), 9)

    def test_water_discount_equal(self):
        order = {"Spicy Dog": 2, "Water": 2}
        self.assertAlmostEqual(bill(order, menu), 10.00)

    def test_water_discount_more_dogs(self):
        order = {"Spicy Dog": 4, "Water": 2}
        self.assertAlmostEqual(bill(order, menu), 20.00)

    def test_water_discount_more_waters(self):
        order = {"Spicy Dog": 2, "Water": 4}
        self.assertAlmostEqual(bill(order, menu), 12.00)

    def test_beer_discount_6(self):
        order = {"Beer": 6}
        self.assertAlmostEqual(bill(order, menu), 25.00)

    def test_beer_discount_12(self):
        order = {"Beer": 12}
        self.assertAlmostEqual(bill(order, menu), 50.00)

    def test_beer_discount_7(self):
        order = {"Beer": 7}
        self.assertAlmostEqual(bill(order, menu), 30.00)

