#!/usr/bin/env python3

class CashRegister:
  
  def __init__(self, discount = 0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.transactions = []

  def add_item(self, title, price, quantity = 1):
    total_price = price * quantity
    self.total += total_price
    self.items.extend([title] * quantity)
    self.transactions.append(total_price)

  def apply_discount(self):
    savings = float(self.total * (self.discount / 100))
    self.total = self.total - savings
    if self.discount == 0:
      print("There is no discount to apply.", end = "\n")
    else:
      print(f"After the discount, the total comes to ${self.total:.0f}.", end = "\n")

  def void_last_transaction(self):
    self.items.pop()
    last_transaction = self.transactions.pop()
    self.total -= last_transaction