import unittest
from bank.bank import (
    open_bank,
    register_customer,
    open_account,
    deposit_money,
    withdraw_money,
    get_customer,
    get_bank,
    get_account,
)

from bank.value_objects import Amount
from bank.repos import bank_data, customer_data


class TestSimpleBank(unittest.TestCase):
    def test_example_scenario(self):
        bank = open_bank("Simple Bank")
        customer = register_customer(bank.id.value, "Alice")
        account = open_account(bank.id.value, customer.id.value, "Alice Savings")

        deposit_amount = 30
        account = deposit_money(account.id.value, deposit_amount)
        self.assertEqual(account.balance.value, 30)
        self.assertEqual(get_customer(customer.id.value).balance.value, deposit_amount)
        self.assertEqual(get_bank(bank.id.value).balance.value, deposit_amount)

        withdraw_amount = 20
        new_balance = 10
        account = withdraw_money(account.id.value, withdraw_amount)
        self.assertEqual(account.balance.value, new_balance)
        self.assertEqual(get_customer(customer.id.value).balance.value, new_balance)
        self.assertEqual(get_bank(bank.id.value).balance.value, new_balance)

        with self.assertRaises(Exception):
            withdraw_money(account.id.value, Amount(20))


if __name__ == "__main__":
    unittest.main()
