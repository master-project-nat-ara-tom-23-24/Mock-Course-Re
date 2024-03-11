You are programming the cashier's system for a hot-dog stand with a menu as shown below.

```
menu = {
  "Hot Dog":      3.50,
  "Spicy Dog":    4.00,
  "Vegan Dog":    3.50,
  "Water":        1.50,
  "Fizzy Drink":  2.50,
  "Beer":         4.00
}
```

However, you offer some special discounts if certain conditions apply:
 * When ordering a Water with a Spicy-Dog, the Water is free. This applies for every pair of these products ordered even if ordering multiple pairs.
 * Every 6th beer in an order is free.

Implement a function `bill` which takes two parameters, a dictionary `order`, which is mapping product names to the number of each item ordered, and a dictionary `menu` which maps product names to the price of each product. The function should return the total sum of the order. If an order does not contain any items, it should raise a ValueError.

