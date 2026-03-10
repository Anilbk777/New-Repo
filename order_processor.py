class InventoryChecker:
    def check_stock(self, item_name: str, quantity: int) -> bool:
        stock = 100
        available = quantity <= stock
        print(f"{item_name}- requested quantity {quantity}, in stock {stock}")
        return available


class PriceCalculator:
    def calculate(self, item_name: str, quantity: int) -> float:
        item_name = item_name.lower()
        prices = {"laptop": 999.99, "mouse": 29.99, "keyborad": 49.99}
        unit_price = prices.get(item_name, 99.99)
        total = unit_price * quantity
        return total


class InvoiceGenerator:
    def generate(self, item_name: str, quantity: int, total: float) -> str:
        return (
            f"\n{'='*35}\n"
            f"  INVOICE\n"
            f"{'='*35}\n"
            f"  Item     : {item_name}\n"
            f"  Quantity : {quantity}\n"
            f"  Total    : ${total:.2f}\n"
            f"{'='*35}\n"
        )


class OrderProcessor:
    def process_order(
        self,
        item_name: str,
        quantity: int,
        checker: InventoryChecker,
        calculator: PriceCalculator,
        generator: InvoiceGenerator,
    ):
        # step 1 — check availability
        if not checker.check_stock(item_name, quantity):
            raise ValueError(
                f"'{item_name}' is out of stock for requested quantity of {quantity}."
            )

        # step 2 — calculate total
        total = calculator.calculate(item_name, quantity)

        # step 3 — generate invoice
        return generator.generate(item_name, quantity, total)


if __name__ == "__main__":
    processor = OrderProcessor()

    checker = InventoryChecker()
    calculator = PriceCalculator()
    generator = InvoiceGenerator()

    invoice = processor.process_order("Laptop", 2, checker, calculator, generator)
    print(invoice)
