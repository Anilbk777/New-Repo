class Passport:
    def __init__(self, passport_number: str):
        self._passport_number = passport_number

    def __repr__(self):
        return f"Passport(passport_number={self._passport_number!r})"


class Person:
    def __init__(self, name: str):
        self.name = name
        self.passport: Passport | None = None   

    def add_passport(self, ppt: Passport):
        if self.passport:
            raise ValueError(f"{self.name} already has a passport")
        self.passport = ppt

    def __repr__(self):
        return f"Person(name={self.name!r}, passport={self.passport})"


# Usage
passport = Passport("A1234567")
alice = Person("Alice")
alice.add_passport(passport)

print(alice)      
# print(alice.passport) 

print(passport)