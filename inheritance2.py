from abc import ABC, abstractmethod

class Payment(ABC):
    def __init__(self,amt, timestmp):
        self.amount = amt
        self.timestamp = timestmp
    @abstractmethod
    def process(self):
        pass

class CreditCardPayment(Payment):

    def __init__(self,amt, timestmp, c_number):
        self.card_number = c_number
        super().__init__(amt, timestmp)

    def process(self):
        print(f"Time- {self.timestamp}")
        print(f"payment through Credit card of number {self.card_number} and amount is {self.amount}")

class UPIPayment(Payment):

    def __init__(self, amt, timestmp, upi_id):
        self.upi_id = upi_id
        super().__init__(amt, timestmp)

    def process(self):
        print(f"Time- {self.timestamp}")

        print(f"payment through UPI of ID {self.upi_id} and amount is {self.amount}")


class CryptoPayment(Payment):
    def __init__(self, amt, timestmp, wallet_address):
        self.wallet_address =  wallet_address
        super().__init__(amt, timestmp)

    def process(self):
        print(f"Time- {self.timestamp}")

        print(f"payment through crypto of address {self.wallet_address} and amount is {self.amount}")




import datetime
import pytz

# Define the time zone for Nepal
nepal_timezone = pytz.timezone('Asia/Kathmandu')

# Get the current time in the specified time zone
current_time_in_nepal = datetime.datetime.now(nepal_timezone)

now = current_time_in_nepal.strftime('%Y-%m-%d %H:%M:%S')


def complete_payment(payment: Payment):
    payment.process()

obj1 = CreditCardPayment(500,now,"2222-4444")
complete_payment(obj1)