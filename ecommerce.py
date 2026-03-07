from __future__ import annotations


class Product:
    def __init__(self, name: str, price: float):
        self._name = name
        self._price = price

    @property
    def name(self) -> str:
        return self._name

    @property
    def price(self) -> float:
        return self._price

    def __repr__(self):
        return f"Product(name={self._name!r}, price={self._price})"


class Catalog:
    def __init__(self, products: list[Product] | None = None):
        self._products: list[Product] = list(products) if products else []

    def add_product(self, product: Product):
        if product in self._products:
            raise ValueError(f"'{product.name}' already exists in the catalog.")
        self._products.append(product)

    def remove_product(self, product: Product):
        if product not in self._products:
            raise ValueError(f"'{product.name}' not found in the catalog.")
        self._products.remove(product)

    def find_by_name(self, name: str) -> Product | None:    
        for product in self._products:
            if product.name == name:
                return product
        return None

    @property
    def product_count(self) -> int:
        return len(self._products)                          

    @property
    def products(self) -> list[Product]:
        return list(self._products)

    def __repr__(self):
        return f"Catalog(products={self.product_count})"


class Cart:
    def __init__(self):
        self._products: list[Product] = []

    def add_item(self, product: Product):
        if product in self._products:
            raise ValueError(f"'{product.name}' is already in your cart.")
        self._products.append(product)
        print(f"'{product.name}' added to cart.")

    def remove_item(self, product: Product):
        if product not in self._products:
            raise ValueError(f"'{product.name}' is not in your cart.")
        self._products.remove(product)

    def clear_cart(self):
        if not self._products:
            raise ValueError("Cart is already empty.")
        self._products = []

    def get_total(self) -> float:
        return sum(product.price for product in self._products) 

    @property
    def item_count(self) -> int:
        return len(self._products)                               

    @property
    def products(self) -> list[Product]:
        return list(self._products)

    def __repr__(self):
        return f"Cart(items={self.item_count}, total={self.get_total()})"


class Customer:
    def __init__(self, name: str):
        self._name = name
        self._cart = Cart()                 

    @property
    def name(self) -> str:
        return self._name

    @property
    def cart(self) -> Cart:
        return self._cart

    def check_out(self):
        if self._cart.item_count == 0:      
            raise ValueError("Your cart is empty.")
        print(f"\n{self._name}'s Order:")
        for product in self._cart.products:
            print(f"  - {product.name}: ${product.price}")
        print(f"  Total: ${self._cart.get_total():.2f}")

    def __repr__(self):
        return f"Customer(name={self._name!r}, cart={self._cart})"


if __name__ == "__main__":
    laptop = Product("Laptop", 999.99)
    mouse = Product("Mouse", 29.99)
    keyboard = Product("Keyboard", 79.99)

    catalog = Catalog()
    catalog.add_product(laptop)
    catalog.add_product(mouse)
    catalog.add_product(keyboard)

    alice = Customer("Alice")
    bob = Customer("Bob")

    alice.cart.add_item(laptop)
    alice.cart.add_item(mouse)

    bob.cart.add_item(laptop)       
    bob.cart.add_item(keyboard)

    print(f"Alice's cart: {alice.cart.item_count} items, ${alice.cart.get_total()}")
    print(f"Bob's cart: {bob.cart.item_count} items, ${bob.cart.get_total()}")

    alice.check_out()
    bob.check_out()

    print(f"\nCatalog still has {catalog.product_count} products")
    print(f"Bob's cart still has {bob.cart.item_count} items")
    print(f"Laptop still exists: {laptop.name}")   