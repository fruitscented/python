class Account:
    def __init__(self, name):
        self.account_name = "John"
        self.account_balance = 100

    def deposit(self, amount):
        try:
            if amount > 0:
                self.account_balance += amount
                return True
            else:
                return False
        except TypeError:
            return False

    def withdraw(self, amount):
        try:
            if amount > 0:
                if self.account_balance >= amount:
                    self.account_balance -= amount
                    return True
                else:
                    return False
        except TypeError:
            return False

    def get_balance(self):
        print(self.account_balance)

    def get_name(self):
        print(self.account_name)
