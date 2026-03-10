from abc import ABC, abstractmethod


class TaxCalculator(ABC):
    @abstractmethod
    def calculate_tax(self, amount: float) -> float:
        pass
