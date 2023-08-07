import unittest
from account import *


class TestAccount(unittest.TestCase):

    def setUp(self):
        self.test_account = Account("John")
        self.test_account.account_balance = 100

    def test_deposit(self):
        self.assertTrue(self.test_account.deposit(100.0))
        self.assertFalse(self.test_account.deposit("a"))
        self.assertFalse(self.test_account.deposit(-1))
        self.assertFalse(self.test_account.deposit(0))

    def test_withdraw(self):
        self.assertTrue(self.test_account.withdraw(100.0))
        self.assertFalse(self.test_account.withdraw("a"))
        self.assertFalse(self.test_account.withdraw(-1))
        self.assertFalse(self.test_account.withdraw(0))
        self.assertFalse(self.test_account.withdraw(200.0))


if __name__ == "__main__":
    unittest.main()