from abc import ABC
from enum import Enum
from bank.value_objects import Name, Amount, UniqueEntityId

MAX_TRANSACTION = Amount(10 ** 6)
MAX_BALANCE = Amount(10 ** 8)


class InsufficientFunds(Exception):
    pass


class InvalidAmount(Exception):
    pass


class AccountSizeExceeded(Exception):
    pass


class Aggregate(ABC):
    def __init__(self, name: Name) -> None:
        self.id = UniqueEntityId()
        self.name = name
        self.balance = Amount(0)
        self.type = type

    def decrease_balance(self, amount: Amount) -> None:
        self.balance -= amount

    def increase_balance(self, amount: Amount) -> None:
        self.balance += amount


class Account(Aggregate):
    def __init__(self, bank_id: UniqueEntityId, customer_id: UniqueEntityId, name: Name):
        self.bank_id = bank_id
        self.customer_id = customer_id
        super(Account, self).__init__(name)

    def withdraw(self, amount: Amount) -> None:
        if self.balance >= amount:
            self.decrease_balance(amount)
        else:
            raise InsufficientFunds

    def deposit(self, amount: Amount) -> None:
        if self.balance + amount <= MAX_BALANCE:
            self.increase_balance(amount)
        else:
            raise AccountSizeExceeded


class Customer(Aggregate):
    def __init__(self, bank_id: UniqueEntityId, name: Name):
        self.bank_id = bank_id
        super(Customer, self).__init__(name)


class Bank(Aggregate):
    def __init__(self, name: Name) -> None:
        super(Bank, self).__init__(name)
