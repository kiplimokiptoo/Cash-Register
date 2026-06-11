#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount
        self.items = []
        self.last_transaction = 0

    def add_item(self, title, price, quantity=1):
        transaction_total = price * quantity
        self.total += transaction_total
        self.last_transaction = transaction_total

        for _ in range(quantity):
            self.items.append(title)

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
            return

        self.total = self.total * (100 - self.discount) / 100
        if self.total == int(self.total):
            self.total = int(self.total)

        print(f"After the discount, the total comes to ${self.total}.")

    def void_last_transaction(self):
        self.total -= self.last_transaction
        if self.total == int(self.total):
            self.total = int(self.total)

        self.last_transaction = 0

        while self.items and self.total < 0:
            self.items.pop()

        if self.total < 0:
            self.total = 0
