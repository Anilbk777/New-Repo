from abc import ABC, abstractmethod


class TaxCalculator(ABC):
    @abstractmethod
    def calculate_tax(self, amount: float) -> float:
        pass


class USTaxCalculator(TaxCalculator):
    def calculate_tax(self, amount: float) -> float:
        return 0.10 * amount


class EUTaxCalculator(TaxCalculator):
    def calculate_tax(self, amount: float) -> float:
        return 0.20 * amount


class UKTaxCalculator(TaxCalculator):
    def calculate_tax(self, amount: float) -> float:
        return 0.15 * amount


class OrderProcessor:
    def __init__(self, region: str, tax_calculator: TaxCalculator):
        self._region = region
        self._tax_calculator = tax_calculator

    def process_order(self, amount: float) -> None:
        data = self.__calculation(amount)
        print(
            f"[{self._region} Order] -> Subtotal: {amount:.2f}, Tax: {data["tax"]:.2f}, Total: {data["total"]:.2f}"
        )

    def __calculation(self, amount: float) -> dict[str, float]:
        tax = self._tax_calculator.calculate_tax(amount)
        total = amount + tax
        return {"tax": tax, "total": total}


if __name__ == "__main__":

    us_order_processr = OrderProcessor("US", USTaxCalculator())
    us_order_processr.process_order(100.00)

    uk_order_processr = OrderProcessor("UK", UKTaxCalculator())
    uk_order_processr.process_order(100.00)
