import unittest
from Python_Practices import bankaccount

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account1 = bankaccount.Account("Olakunle", "Iyanda")

    def test_that_account_exist(self):
        bankaccount.Account("Olakunle", "Iyanda")

    def test_that_can_be_created(self):
        account1 = bankaccount.Account("Olakunle", "Iyanda")
        self.assertEqual(account1.first_name, "Olakunle")
        self.assertEqual(account1.last_name, "Iyanda")

    def test_that_account_balance_is_zero(self):
        account1 = bankaccount.Account("Olakunle", "Iyanda")
        self.assertEqual(account1.balance, 0)

    def test_that_account_can_deposit(self):
        account1 = bankaccount.Account("Olakunle", "Iyanda")
        account1.deposit(5000)
        self.assertEqual(account1.balance, 5000)

    def test_that_account_cannot_deposit_negative_amount(self):
        account1 = bankaccount.Account("Olakunle", "Iyanda")
        account1.deposit(-5000)
        self.assertRaises(ValueError, account1.deposit, -5000)

    def test_that_account_can_withdraw(self):
        account1 = bankaccount.Account("Olakunle", "Iyanda")
        account1.deposit(5000)
        account1.withdraw(3000)
        self.assertEqual(account1.balance, 2000)

    def test_that_account_cannot_withdraw_over_draft(self):
        account1 = bankaccount.Account("Olakunle", "Iyanda")
        account1.deposit(5000)
        account1.withdraw(7000)
        self.assertRaises(ValueError, account1.withdraw, 7000)

    def test_that_account_cannot_withdraw_negative_amount(self):
        account1 = bankaccount.Account("Olakunle", "Iyanda")
        account1.deposit(5000)
        account1.withdraw(-3000)
        self.assertRaises(ValueError, account1.withdraw, -3000)
