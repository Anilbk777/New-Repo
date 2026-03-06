from abc import ABC, abstractmethod


class Shape(ABC):
 

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass

    def describe(self):
        print(
            f"Shape: [{self.name}] | Area: [{self.area():.2f}] | Perimeter:[{self.perimeter():.2f}]"
        )


class Circle(Shape):
    PI = 3.14
    def __init__(self, radius: float):
        super().__init__("Circle")
        self.radius = radius

    def area(self) -> float:
        return self.PI * (self.radius**2)

    def perimeter(self) -> float:
        return 2 * self.PI * self.radius


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)
