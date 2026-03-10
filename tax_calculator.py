from abc import ABC, abstractmethod


class TaxCalculator(ABC):
    @abstractmethod
    def calculate_tax(self, amount: float) -> float:
        pass


class USTaxCalculator(TaxCalculator):
    def calculate_tax(self, amount: float) -> float:
        return 0.10 * amount
