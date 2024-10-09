class Account:
    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.balance = 0.00
        self.account_number = 0

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Negative amount cannot be deposited")
        self.balance += amount

    def withdraw(self, amount):
        if amount < self.balance:
           self.balance -= amount
        else:
            raise ValueError("Insufficient funds")
        if amount < 0:
            raise ValueError("Negative amount cannot be withdrawn")