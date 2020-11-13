import uuid
from abc import ABC
from enum import Enum
from bank.value_objects import Name, Amount

MAX_TRANSACTION = 10 ** 6
MAX_BALANCE = 10 ** 8


class InsufficientFunds(Exception):
    pass


class InvalidAmount(Exception):
    pass


class AccountSizeExceeded(Exception):
    pass


class AggregateType(Enum):
    BANK = 0
    CUSTOMER = 1
    ACCOUNT = 2


class Aggregate(ABC):
    def __init__(self, name: Name, type: AggregateType) -> None:
        self.id = uuid.uuid1()
        self.name = name
        self.balance = Amount(0)
        self.type = type
        self.save()

    def save(self) -> None:
        data[self.type][self.id] = self


class Bank(Aggregate):
    def __init__(self, name: Name) -> None:
        super(Bank, self).__init__(name, AggregateType.BANK)

    @classmethod
    def get(cls, id: int):
        return data[AggregateType.BANK][id]


class Account(Aggregate):
    def __init__(self, bank_id: str, customer_id: str, name: Name):
        self.bank_id = bank_id
        self.customer_id = customer_id
        super(Account, self).__init__(name, AggregateType.ACCOUNT)

    @classmethod
    def get(cls, id: int):
        return data[AggregateType.ACCOUNT][id]

    def withdraw(self, amount: Amount) -> None:
        if self.balance >= amount:
            self.balance -= amount
            self.save()
        else:
            raise InsufficientFunds

    def deposit(self, amount: Amount) -> None:
        new_balance = self.balance + amount
        if new_balance.value <= MAX_BALANCE:
            self.balance = new_balance
            self.save()
        else:
            raise AccountSizeExceeded


class Customer(Aggregate):
    def __init__(self, bank_id: str, name: Name):
        self.bank_id = bank_id
        super(Customer, self).__init__(name, AggregateType.CUSTOMER)

    @classmethod
    def get(cls, id):
        return data[AggregateType.CUSTOMER][id]


# simulate persistence
data = {AggregateType.BANK: {}, AggregateType.CUSTOMER: {}, AggregateType.ACCOUNT: {}}
