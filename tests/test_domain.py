import unittest
from bank.domain import Account, InsufficientFunds, Bank, Customer
from bank.value_objects import Amount, Name, InvalidNameError, UniqueEntityId


class TestDomain(unittest.TestCase):
    def test_account(self):
        name = "Test Account"
        account = Account("1", "1", Name(name))
        self.assertEqual(account.name.value, name)
        self.assertEqual(account.balance, Amount(0))

        account.deposit(Amount(10))
        self.assertEqual(account.balance, Amount(10))

        account.withdraw(Amount(9))
        self.assertEqual(account.balance, Amount(1))

        account.withdraw(Amount(1))
        self.assertEqual(account.balance, Amount(0))

        with self.assertRaises(InsufficientFunds):
            account.withdraw(Amount(1))

        with self.assertRaises(InvalidNameError):
            Account("1", "1", Name(""))

    def test_balance_limit(self):
        account = Account("1", "1", "savings")
        balance = 0
        deposit = 10 ** 6
        while balance + deposit <= 10 ** 8:
            account.deposit(Amount(deposit))
            balance += deposit

        with self.assertRaises(Exception):
            account.deposit(Amount(deposit))

    def test_bank(self):
        name = "Test Bank"
        bank = Bank(Name(name))
        self.assertEqual(bank.name.value, name)
        self.assertEqual(bank.balance.value, 0)

        bank.increase_balance(Amount(100))
        self.assertEqual(bank.balance.value, 100)
        bank.decrease_balance(Amount(100))
        self.assertEqual(bank.balance.value, 0)

        with self.assertRaises(InvalidNameError):
            Bank(Name(""))

    def test_customer(self):
        name = "Test Customer"
        customer = Customer(1, Name(name))
        self.assertEqual(customer.name.value, name)

        customer.increase_balance(Amount(10 ** 6))
        self.assertEqual(customer.balance.value, 10 ** 6)
        customer.decrease_balance(Amount(1))
        self.assertEqual(customer.balance.value, 10 ** 6 - 1)

        with self.assertRaises(InvalidNameError):
            Customer("1", Name(""))
