from typing import List
class FoodOrder:
    def __init__(self, order_id, customer_id) -> None:
        self._order_id =  order_id
        self._customer_id = customer_id
        self._items: List[str] = []
        self._total_amount = 0
        self._is_placed: bool = False

    # Only allow adding items before the order is placed.
    def add_item(self, name:str, price: float) -> None:
        if self._is_placed:
            print("Cannot modify a placed order.")
            return
        self._items.append(name)
        self._total_amount += price

    def place_order(self) ->bool:
        if self._is_placed or not self._items:
            return False
        self._is_placed = True
        return True
    
    def get_item_count(self) -> int:
        return len(self._items)

    def display_order(self) -> None:
        status = "PLACED" if self._is_placed else "PENDING"
        print(f"Order =>{self._order_id}  ({self._customer_id}) - status: {status}")
        for item in self._items:
            print(f" - {item}")
        
        print(f"Total : Rs {self._total_amount:.2f}")


if __name__ == "__main__":
    order1 = FoodOrder("ORD-101","Alice")
    order1.add_item("Pizza",12.99)
    order1.add_item("Garlic Bread", 4.99)
    order1.add_item("Coke", 2.49)
    order1.place_order()

    order2 = FoodOrder("ORD-102", "Bob")
    order2.add_item("Burger", 9.99)
    order2.add_item("Fries", 3.99)

    order1.display_order()
    print("*"*60)
    order2.display_order()
