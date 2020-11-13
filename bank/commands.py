from abc import ABC, abstractmethod
from bank.domain import Bank, Customer, Account
from bank.events import MoneyDeposited, MoneyWithdrawn
from bank.value_objects import Amount


class InvalidName(Exception):
    pass


class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass


class OpenBank(Command):
    def __init__(self, bank_name: str) -> None:
        self._bank_name = bank_name

    def execute(self) -> str:
        bank = Bank(self._bank_name)
        return bank.id


class RegisterCustomer(Command):
    def __init__(self, bank_id: str, customer_name: str) -> None:
        self._bank_id = bank_id
        self._customer_name = customer_name

    def execute(self) -> str:
        customer = Customer(self._bank_id, self._customer_name)
        return customer.id


class OpenAccount(Command):
    def __init__(self, customer_id: str, account_name: str) -> None:
        self._customer_id = customer_id
        self._account_name = account_name

    def execute(self) -> str:
        customer = Customer.get(self._customer_id)
        account = Account(customer.bank_id, self._customer_id, self._account_name)
        return account.id


class DepositMoney(Command):
    def __init__(self, account_id: str, amount: Amount) -> None:
        self._account_id = account_id
        self._amount = amount

    def execute(self) -> str:
        account = Account.get(self._account_id)
        account.deposit(self._amount)

        event = MoneyDeposited(account.bank_id, account.customer_id, self._amount)
        event.trigger()
        return


class WithdrawMoney(Command):
    def __init__(self, account_id: str, amount: Amount) -> None:
        self._account_id = account_id
        self._amount = amount

    def execute(self) -> str:
        account = Account.get(self._account_id)
        account.withdraw(self._amount)

        event = MoneyWithdrawn(account.bank_id, account.customer_id, self._amount)
        event.trigger()
        return
