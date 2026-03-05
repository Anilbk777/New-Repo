from enum import Enum

class HTTPStatus(Enum):
    OK = (200, "ok")
    BAD_REQUEST = (400, "Bad Request")
    NOT_FOUND = (404, "Not Found")
    INTERNAL_SERVER_ERROR = (500, "Internal Server Error")

    def __init__(self, code, message):
        self.code = code
        self.message = message

    def is_success(self) -> bool:
        return self.code < 400

    def display(self) -> None:
        print(f"{self.code} {self.message}")

    @staticmethod
    def from_code(code: int):
        for status in HTTPStatus:
            if status.code == code:
                return status
        return None

    @classmethod
    def from_codey(cls, code: int):
        for status in cls:
            if code == status.code:
                return status

        return None


if __name__ == "__main__":
    HTTPStatus.BAD_REQUEST.display()
    HTTPStatus.OK.display()

    print(f"Is 200 success: {str(HTTPStatus.OK.is_success()).lower()}")
    print(f"Is 400 success: {str(HTTPStatus.BAD_REQUEST.is_success()).lower()}")

    found = HTTPStatus.from_codey(500)
    print(found)
