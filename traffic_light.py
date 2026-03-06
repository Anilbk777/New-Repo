<<<<<<< HEAD
from enum import Enum


class TrafficLight(Enum):
    # Set values to duration: RED = 30, YELLOW = 5, GREEN = 25
    RED = 30
    YELLOW = 5
    GREEN = 25

    def next(self) -> "TrafficLight":
        # Return next light: RED->GREEN, GREEN->YELLOW, YELLOW->RED
        members = list(TrafficLight)
        current_index = members.index(self)
        next_index = (current_index + 1) % len(members)
        return members[next_index]


    def display(self) -> None:
        # Print: "COLOR (Xs)" e.g. "RED (30s)"
        print(f"{self.name} ({self.value}s)")


if __name__ == "__main__":
    light = TrafficLight.RED
    for _ in range(6):
        light.display()
        light = light.next()
=======
from enum import Enum


class TrafficLight(Enum):
    # Set values to duration: RED = 30, YELLOW = 5, GREEN = 25
    RED = 30
    YELLOW = 5
    GREEN = 25

    def next(self) -> "TrafficLight":
        # Return next light: RED->GREEN, GREEN->YELLOW, YELLOW->RED
        members = list(TrafficLight)
        current_index = members.index(self)
        next_index = (current_index + 1) % len(members)
        return members[next_index]


    def display(self) -> None:
        # Print: "COLOR (Xs)" e.g. "RED (30s)"
        print(f"{self.name} ({self.value}s)")


if __name__ == "__main__":
    light = TrafficLight.RED
    for _ in range(6):
        light.display()
        light = light.next()
>>>>>>> 64568799ad5ad97ec896ddba5369d8050459014c
