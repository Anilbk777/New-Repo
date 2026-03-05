from abc import ABC, abstractmethod
from typing import List


class Validator(ABC):

    @abstractmethod
    def validate(self, input: str) -> bool:
        pass


class EmailValidator(Validator):
    def validate(self, input: str) -> bool:
        return "@" in input


class PasswordVlaidator(Validator):
    def validate(self, input: str) -> bool:
        return len(input) >= 8


class RegistrationService:
    def __init__(self, validators: List[Validator] | None = None):
        self.validators = validators or []

    def register(self, input: str) -> None:
        result = all(validator.validate(input) for validator in self.validators)

        if result:
            print(f"{input} - PASSED")
        else:
            print(f"{input} - Failed")

    def another_register(self, input: str) -> bool:
        for validator in self.validators:
            if not validator.validate(input):
                return False
        return True


if __name__ == "__main__":
    validators = [EmailValidator(), PasswordVlaidator()]

    register1 = RegistrationService(validators)
    input = "anil@gmail.com"
    input2 = "short@"
    register1.register(input)
    register1.register(input2)
