from typing import Dict
from uuid import UUID
from bank.domain import Account, Customer, Bank, Aggregate
from bank.value_objects import UniqueEntityId


class AccountRepo(object):
    @classmethod
    def save(cls, account: Account):
        account_data[account.id.value] = account

    @classmethod
    def findById(cls, id: UniqueEntityId):
        return account_data[id.value]


class CustomerRepo(object):
    @classmethod
    def save(cls, customer: Customer):
        customer_data[customer.id.value] = customer

    @classmethod
    def findById(cls, id: UniqueEntityId):
        return customer_data[id.value]


class BankRepo(object):
    @classmethod
    def save(cls, bank: Bank):
        bank_data[bank.id.value] = bank

    @classmethod
    def findById(cls, id: UniqueEntityId):
        return bank_data[id.value]


# simulate persistence
account_data: Dict[UUID, Aggregate] = {}
customer_data: Dict[UUID, Aggregate] = {}
bank_data: Dict[UUID, Aggregate] = {}