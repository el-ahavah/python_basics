class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"{self.owner} deposited ₦{amount}")

    def show_balance(self):
        print(f"{self.owner}'s balance is ₦{self.balance}")