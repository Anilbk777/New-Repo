class BankAccount:
  def __init__(self, owner_name: str, account_number: str, balance:float):
    self._owner_name =  owner_name
    self._account_number = account_number
    self._balance = balance

  def deposit(self, amount: float) ->bool:
    if amount <= 0 :
      print("Amount must me positive.")
      return False
    self._balance += amount
    print("amount added successfully.")

  def withdraw(self, amount:float) -> bool:
    if amount <= 0:
      print("Negative amount can't be withdraw")
      return False

    if amount > self._balance:
      print("Insufficient balance.")
      return False

    self._balance -=amount
    return True

  def display_account(self) -> None:
    print(f"Owner name: {self._owner_name} | Account number: {self._account_number} | Balance: {self._balance:.2f}")


class SavingsAccount(BankAccount):
  def __init__(self, owner_name: str, account_number: str, balance: float, interest_rate:float):
    super().__init__(owner_name, account_number, balance)
    self._interest_rate = interest_rate

  # def withdraw(self, amount: float) -> bool:
  #   if self._balance < 100:
  #     print("Withdrawl failed! There must be minimum balance of 100")
  #     return False

  #   self._balance -= amount
  #   return True

  def withdraw(self, amount: float) -> bool:
    minimum_balance = 100

    if amount <= 0:
      print("Amount must be positive.")
      return False

    if (self._balance - amount) < minimum_balance:
      print("Withdrawal failed! Minimum balance of 100 must remain.")
      return False

    self._balance -= amount
    print(f"Withdraw {amount} successfully.")
    return True

  def apply_interest(self):
    self._balance += self._balance * self._interest_rate / 100
    print("Interest rate applied.")
    return self._balance

class CheckingAccount(BankAccount):
  def __init__(self, owner_name: str, account_number: str,balance:float, overdraft_limit: float):
    super().__init__(owner_name, account_number, balance)
    self._overdraft_limit = overdraft_limit

  def withdraw(self, amount: float) -> bool:
    if amount > (self._balance + self._overdraft_limit):
      print("Entered amount can't be withdraw, it surpass the balance plus overdraft limit.")
      return False
    self._balance -= amount
    print("amount withdraw successfully.")
    return True



if __name__ == "__main__":
    savings = SavingsAccount("Alice", "SAV-001", 1000, 2.0)
    savings.display_account()
    print(f"Withdraw $950: {str(savings.withdraw(950)).lower()}")
    savings.apply_interest()
    savings.display_account()

    print()

    checking = CheckingAccount("Bob", "CHK-002", 500, 300)
    checking.display_account()
    print(f"Withdraw $700: {str(checking.withdraw(700)).lower()}")
    checking.display_account()
