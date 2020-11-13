import unittest
from bank.domain import Account, InsufficientFunds, Bank, Customer
from bank.value_objects import Amount, Name, InvalidNameError


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

    def test_bank(self):
        name = "Test Bank"
        bank = Bank(Name(name))
        self.assertEqual(bank.name.value, name)

        with self.assertRaises(InvalidNameError):
            Bank(Name(""))

    def test_customer(self):
        name = "Test Customer"
        customer = Customer(1, Name(name))
        self.assertEqual(customer.name.value, name)

        with self.assertRaises(InvalidNameError):
            Customer("1", Name(""))
