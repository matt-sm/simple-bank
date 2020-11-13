import unittest
from bank.bank import (
    open_bank,
    register_customer,
    open_account,
    deposit_money,
    withdraw_money,
    get_account_balance,
    get_customer_balance,
    get_bank_balance,
)

from bank.value_objects import Amount


class TestSimpleBank(unittest.TestCase):
    def test_example_scenario(self):
        bank_id = open_bank("Simple Bank")
        customer_id = register_customer(bank_id, "Alice")
        account_id = open_account(customer_id, "Alice Savings")

        deposit_amount = Amount(30)
        deposit_money(account_id, deposit_amount)
        self.assertEqual(get_account_balance(account_id), deposit_amount)
        self.assertEqual(get_customer_balance(customer_id), deposit_amount)
        self.assertEqual(get_bank_balance(bank_id), deposit_amount)

        withdraw_amount = Amount(20)
        new_balance = Amount(10)
        withdraw_money(account_id, withdraw_amount)
        self.assertEqual(get_account_balance(account_id), new_balance)
        self.assertEqual(get_customer_balance(customer_id), new_balance)
        self.assertEqual(get_bank_balance(bank_id), new_balance)

        with self.assertRaises(Exception):
            withdraw_money(account_id, Amount(20))

    def test_balances(self):
        for b in range(1, 10):
            bank_id = open_bank(f"Bank{b}")
            bank_balance = 0
            accounts = []
            for c in range(1, 10):
                customer_id = register_customer(bank_id, f"Customer{c}")
                customer_balance = 0
                for a in range(1, 10):
                    account_id = open_account(customer_id, f"Customer{c} Account{a}")
                    accounts.append(account_id)
                    balance = 0
                    for m in range(1, 10):
                        balance += m
                        customer_balance += m
                        bank_balance += m
                        deposit_money(account_id, Amount(m))
                    self.assertEqual(get_account_balance(account_id), Amount(balance))
                self.assertEqual(get_customer_balance(customer_id), Amount(customer_balance))
            self.assertEqual(get_bank_balance(bank_id), Amount(bank_balance))

            for a in accounts:
                withdraw_money(a, get_account_balance(a))
                self.assertEqual(get_account_balance(a), Amount(0))

            self.assertEqual(get_bank_balance(bank_id), Amount(0))

    def test_balance_limit(self):
        bank_id = open_bank("Simple Bank")
        customer_id = register_customer(bank_id, "Alice")
        account_id = open_account(customer_id, "Alice Savings")
        balance = 0
        deposit = 10 ** 6
        while balance + deposit <= 10 ** 8:
            deposit_money(account_id, Amount(deposit))
            balance += deposit

        with self.assertRaises(Exception):
            deposit_money(account_id, Amount(deposit))


if __name__ == "__main__":
    unittest.main()
