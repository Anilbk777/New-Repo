class Vehicle:
    def __init__(self,model,price):
        self.model = model
        self.price = price

    def start(self):
        print("Starting Vehicle")

    def stop(self):
        print("Stop Vehicle")
    
    def detail(self):
        print(f"The price of the model '{self.model}' is {self.price} ")

class Car(Vehicle):
    def open_trunk(self):
        print("Opening trunk of car")

class Bike(Vehicle):
    def kick_start(self):
        print("Bike start from kicking.")


if __name__ == "__main__":
    car1 = Car("maruti",80000)
    bike1 = Bike("Royal Enfield",50000)
    
    car1.detail()
    bike1.detail()

    car1.open_trunk()
    bike1.kick_start()
