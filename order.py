class LineItem:
  def __init__(self, product_name:str, quantity: int, unit_price:float):
    self._product_name = product_name
    self._quantity = quantity
    self._unit_price = unit_price

  def get_subtotal(self) -> float:
    return self._quantity * self._unit_price

  @property
  def product_name(self):
    return self._product_name

  @property
  def quantity(self):
    return self._quantity

  @property
  def unit_price(self):
    return self._unit_price

  def __str__(self):
    return (f"{self._product_name} x{self._quantity} "
            f"@ ${self._unit_price:.2f} = ${self.get_subtotal():.2f}")


  def __repr__(self):
    return f"LineItem(product_name ={self.product_name!r}, quantity={self.quantity!r}, unit_price={self.unit_price!r})"

class Order:
  def __init__(self, order_id:str):
    self._order_id = order_id
    self._line_items :list[LineItem] = []

  def add_item(self, product_name:str, quantity:int, unit_price: float):
    for item in self._line_items:
      if item.product_name == product_name:
        raise ValueError(f"{product_name} is already in {self._order_id}")

    self._line_items.append(LineItem(product_name,quantity, unit_price))

  def remove_item(self, product_name:str):
    for item in self._line_items:
      if item.product_name == product_name:
        self._line_items.remove(item)
        return 
    raise ValueError(f"'{product_name}' not found in order '{self._order_id}'.")

  def update_quantity(self, product_name:str, quantity:int):
    for item in self._line_items:
      if item.product_name == product_name:
        index = self._line_items.index(item)
        self._line_items[index] = LineItem(product_name, quantity, item.unit_price)
        return 
    raise ValueError(f"'{product_name}' not found in order '{self._order_id}'.")

  def get_total(self):
    return sum(item.get_subtotal() for item in self._line_items)

  def print_receipt(self):
    print(f"\nOrder: {self._order_id}")
    print("-" * 45)
    for item in self._line_items: 
      print(f"  {item}")              
    print("-" * 45)
    print(f"  Total: ${self.get_total():.2f}")

  @property
  def order_id(self) -> str:
      return self._order_id

  @property
  def line_items(self) -> list[LineItem]:
      return list(self._line_items)           

  @property
  def item_count(self) -> int:
      return len(self._line_items)

  def __repr__(self):
      return f"Order(order_id={self._order_id!r}, items={self.item_count}, total={self.get_total():.2f})"



if __name__ == "__main__":
  order = Order("ORD-1001")
  order.add_item("Wireless Mouse", 2, 29.99)
  order.add_item("USB-C Cable", 3, 9.99)
  order.add_item("Laptop Stand", 1, 49.99)

  order.print_receipt()

  order.update_quantity("USB-C Cable", 5)
  order.remove_item("Laptop Stand")

  print("\nAfter update:")
  order.print_receipt()



