class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.__balance += amount
        return self.__balance
    
    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("Insufficient balance")
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.__balance -= amount
        return self.__balance

    def get_balance(self):
        return self.__balance
    

def menu():
        account = BankAccount()

        while True:
            print("""
   Namaste User!
        1. Deposit
        2. Withdraw
        3. Check Balance
        4. Exit
"""
            )

            user_input = input("Enter your choice: ")

            if user_input == "1":
                #deposit
                try:
                    amount = float(input("Enter amount: "))
                    new_balance = account.deposit(amount)
                    print(f"Deposited sucessfully! New balance: {new_balance}")

                except ValueError as e:
                    print("Error: ",e)

            elif user_input == "2":
                #withdraw
                try:
                    amount = float(input("Enter amount: "))
                    new_balance = account.withdraw(amount)
                    print(f"Withdrawn successfully! New Balance: {new_balance}")
                except ValueError as e:
                    print("Error: ",e)

            elif user_input == "3":
                #get_balance
                print("Current balance: ", account.get_balance())
            elif user_input == "4":
                print("Thank you for using ATM!")
                break
            else:
                print("Invalid Input")


if __name__ == "__main__":
    menu()
   
            





            
        
    
    