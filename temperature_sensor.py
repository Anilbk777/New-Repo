from typing import List


class TempretaureSensor:
    def __init__(self):
        self.__reading: List[float] = []

    def addReading(self, value: float) -> None:
        if value >= -50 and value <= 150:
            self.__reading.append(value)
            print("Value is added successfully")
        else:
            print("value must be between -50 to 150 degree")

    def getAverage(self) -> float:
        return sum(self.__reading) / len(self.__reading)

    def getReadingCount(self) -> int:
        return len(self.__reading)

    def getReading(self) -> List[float]:
        return self.__reading.copy()


if __name__ == "__main__":
    temp = TempretaureSensor()
    temp.addReading(40)
    temp.addReading(-50)
    temp.addReading(-60)
    temp.addReading(-30)
    temp.addReading(100)
    temp.addReading(120)

    result = temp.getAverage()
    print(result)

    output = temp.getReading()
    output.append(200)
    print(output)

    output1 = temp.getReading()
    print(output1)

    x = temp.getReadingCount()
    print(x)
