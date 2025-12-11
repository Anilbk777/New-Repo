class Laptop:
    def __init__(self, brand,ram):
        self.brand = brand
        self.ram = ram
    def run(self):
        print("Information of  laptop!")

class Student:
    def __init__(self,name, address,laptop):
        self.name =name
        self.address = address
        self.laptop =laptop

    def info(self):
        print(f"Name = {self.name}")
        print(f"address = {self.address}")
        print(f"laptop_brand = {self.laptop.brand}")
        print(f"laptop_ram = {self.laptop.ram}")

def func(std:Student):
    std.laptop.run()
    std.info()

laptop1 = Laptop("Dell","8GB Ram")
student1 = Student("Anil","pokhara",laptop1)

func(student1)