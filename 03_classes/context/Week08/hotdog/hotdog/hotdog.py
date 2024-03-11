#!/usr/bin/env python3

mc_menu = {
  "Hot Dog":             3.50,
  "Spicy Dog":           4.00,
  "Vegan Dog":           3.50,
  "Water":               1.50,
  "Fizzy Drink":         2.50,
  "Beer":                4.00
}

def bill(order, menu):
    # order cannot be empty
    if order == {}:
        raise ValueError
    total = 0
    # calculate total without discounts
    for item, amount in order.items():
        total += menu[item] * amount
    # water discount
    if "Spicy Dog" in order and "Water" in order:
        free_waters = min([order["Spicy Dog"], order["Water"]])
        total -= free_waters * menu["Water"]
    # beer discount
    if "Beer" in order:
        free_beers = order["Beer"] // 6
        total -= free_beers * menu["Beer"]

    return total

my_order = {
    "Hot Dog": 1,
    "Beer": 1
}
print(bill(my_order, mc_menu))

