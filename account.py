class Account:
    def __init__(self, name):
        self.account_name = "John"
        self.account_balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount):
        if self.account_balance >= amount
            self.account_balance -= amount
            return True
        else:
            return False

    def get_balance(self):
        print(self.account_balance)

    def get_name(self):
        print(self.account_name)