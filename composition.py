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
        return self.price * self.quantity


class OrderSummary:
    def __init__(self,items):
        self.items = items

    def calculate_total(self, tax_percent=5, discount=0):
        subtotal = sum(item.get_total() for item in self.items )
        tax =subtotal * tax_percent / 100
        final_total = subtotal + tax - discount

        return {
            "subtotal" : subtotal,
            "tax" : tax,
            "discount": discount,
            "final_total" :final_total
        }



class Order:
    def __init__(self,customer_name, email, phn, street, city, country):
        self.customer = CustomreInfo(customer_name, email , phn)
        self.address = ShippingAddress(street, city, country)
        self.payment = PaymentDetails()
        self.items = []
        self.summary = OrderSummary(self.items)

    def add_item(self, name, price, quantity):
        item = OrderItem(name, price, quantity)
        self.items.append(item)

    def get_summary(self):
        return self.summary.calculate_total()


sett = ["Name", "Email", "Phone", "Street","city", "country"]
new_lst = []
for i in sett:
    inputt = input(f"Enter {i}: ")
    new_lst.append(inputt)

order = Order(
    new_lst[0],
    new_lst[1],
    new_lst[2],
    new_lst[3],
    new_lst[4],
    new_lst[5]
)


product_name = input("Product Name: ")
price = float(input("Price: "))
quantity = int(input("Quantity: "))

order.add_item(product_name,price,quantity)

summary = order.get_summary()
print(summary)

order.payment.cash()
order.payment.status("Paid")