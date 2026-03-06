from abc import ABC, abstractmethod


class Formatter(ABC):

    @abstractmethod
    def format(self, message: str) -> str:
        pass


class PlainFormatter(Formatter):
    def format(self, message: str) -> str:
        print(f"log = {message}")


class JSONFormatter(Formatter):
    def format(self, message: str) -> str:
        print({"log": message})


class Logger:
    def __init__(self, formatter: Formatter):
        self.formatter = formatter

    def log(self, message: str) -> str:
        self.formatter.format(message)


if __name__ == "__main__":
    logger1 = Logger(PlainFormatter())
    logger1.log("Server started on port 8080")

    logger2 = Logger(JSONFormatter())
    logger2.log("Server started on port 8080")
