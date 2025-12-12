# E-Commerce Order System

class CustomreInfo:
    def __init__(self,name,email,phone):
        self.name = name
        self.email = email
        self.phone = phone

class ShippingAddress:
    def __init__(self,street, city, country):
        self.street = street
        self.city = city
        self.country = country

class PaymentDetails:
    def cash(self):
        print("Payment through Cash")

    def card(self):
         print("Payment through Card")

    def status(self, status):
        if status == "Pending":
            print("Status = Pending")
        else:
            print("status = paid")


class OrderItem:
    def __init__(self,product_name, price, quantity):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity

    def get_total(self):
        return {self.price} * {self.quantity}


class OrderSummary:
    def __init__(self,items):
        self.items = items

    def calculate_total(self, tax_percent=5, discount=0):
        subtotal = sum(self.item.price * self.item.quantity for item in self.items )
        tax =subtotal * tax_percent / 100
        final_total = subtotal + tax - discount

        return {
            "subtotal" : subtotal,
            "tax" : tax,
            "discount": discount,
            "final_total" :final_total
        }



class Order:
    def __init__(self):
        self.customer = CustomreInfo(self.customer_name, self.email, self.phone)
        self.address = ShippingAddress()
        self.payment = PaymentDetails()
        self.items = []
        self.summary = OrderSummary(self.items)

    def add_item(self, name, price, quantity):
        item = OrderItem(name, price, quantity)
        self.items.append(item)

    def get_summary(self):
        return self.summary.calculate_total()
