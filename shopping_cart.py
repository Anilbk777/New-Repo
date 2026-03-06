<<<<<<< HEAD
from typing import Dict


class ShoppingCart:

    DISCOUNT_CODES = {"SAVE10": 0.10}

    def __init__(self):
        self._items: Dict[str, Dict[str, float | int]] = {}
        self._discount_rate: float = 0.0
        self._checked_out: bool = False

    def add_item(self, name: str, price: float) -> None:

        if self._checked_out:
            print("Cannot add item. Cart already checked out.")
            return

        if name in self._items:
            self._items[name]["qty"] += 1

        else:
            self._items[name] = {"price": price, "qty": 1}
        print("Item added successfully.")

    def apply_code(self, code: str) -> bool:

        if self._checked_out:
            print("Cannot apply discount after checkout.")
            return False

        if self._discount_rate > 0:
            print("Discount already applied.")
            return False

        if code not in self.DISCOUNT_CODES:
            print("Invalid discount code.")
            return False

        self._discount_rate = self.DISCOUNT_CODES[code]
        return True

    # def get_total(self) -> float:

    #     subtotal = sum(self._items.values())
    #     discount = subtotal * self._discount_rate

    #     return subtotal - discount
    def get_total(self) -> float:

        total = 0

        for item in self._items.values():
            total += item["price"] * item["qty"]

        if self._discount_rate:
            total = total * 0.9

        return total

    def checkout(self) -> bool:

        if not self._items:
            print("Cart is empty.")
            return False

        if self._checked_out:
            print("Cart already checked out.")
            return False

        self._checked_out = True
        return True


if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_item("Laptop", 999.99)
    cart.add_item("Laptop", 999.99)

    cart.add_item("Mouse", 29.99)

    print(f"Total: ${cart.get_total():.2f}")  # 1029.98

    print(f"Discount: {str(cart.apply_code('SAVE10')).lower()}")  # true
    print(f"Total: ${cart.get_total():.2f}")  # 926.98

    print(f"Discount: {str(cart.apply_code('SAVE10')).lower()}")  # false

    cart.checkout()
    cart.add_item("Keyboard", 79.99)  # Should be rejected
    print(f"Total: ${cart.get_total():.2f}")
=======
from typing import Dict


class ShoppingCart:

    DISCOUNT_CODES = {"SAVE10": 0.10}

    def __init__(self):
        self._items: Dict[str, Dict[str, float | int]] = {}
        self._discount_rate: float = 0.0
        self._checked_out: bool = False

    def add_item(self, name: str, price: float) -> None:

        if self._checked_out:
            print("Cannot add item. Cart already checked out.")
            return

        if name in self._items:
            self._items[name]["qty"] += 1

        else:
            self._items[name] = {"price": price, "qty": 1}
        print("Item added successfully.")

    def apply_code(self, code: str) -> bool:

        if self._checked_out:
            print("Cannot apply discount after checkout.")
            return False

        if self._discount_rate > 0:
            print("Discount already applied.")
            return False

        if code not in self.DISCOUNT_CODES:
            print("Invalid discount code.")
            return False

        self._discount_rate = self.DISCOUNT_CODES[code]
        return True

    # def get_total(self) -> float:

    #     subtotal = sum(self._items.values())
    #     discount = subtotal * self._discount_rate

    #     return subtotal - discount
    def get_total(self) -> float:

        total = 0

        for item in self._items.values():
            total += item["price"] * item["qty"]

        if self._discount_rate:
            total = total * 0.9

        return total

    def checkout(self) -> bool:

        if not self._items:
            print("Cart is empty.")
            return False

        if self._checked_out:
            print("Cart already checked out.")
            return False

        self._checked_out = True
        return True


if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_item("Laptop", 999.99)
    cart.add_item("Laptop", 999.99)

    cart.add_item("Mouse", 29.99)

    print(f"Total: ${cart.get_total():.2f}")  # 1029.98

    print(f"Discount: {str(cart.apply_code('SAVE10')).lower()}")  # true
    print(f"Total: ${cart.get_total():.2f}")  # 926.98

    print(f"Discount: {str(cart.apply_code('SAVE10')).lower()}")  # false

    cart.checkout()
    cart.add_item("Keyboard", 79.99)  # Should be rejected
    print(f"Total: ${cart.get_total():.2f}")
>>>>>>> 64568799ad5ad97ec896ddba5369d8050459014c
