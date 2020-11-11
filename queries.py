from abc import ABC, abstractmethod
from domain import Bank, Customer, Account


class Query(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass


class GetAccountBalance(Query):
    def __init__(self, account_id: str) -> None:
        self._account_id = account_id

    def execute(self) -> str:
        account = Account.get(self._account_id)
        return account.balance


class GetCustomerBalance(Query):
    def __init__(self, customer_id: str) -> None:
        self._customer_id = customer_id

    def execute(self) -> str:
        customer = Customer.get(self._customer_id)
        return customer.balance


class GetBankBalance(Query):
    def __init__(self, bank_id: str) -> None:
        self._bank_id = bank_id

    def execute(self) -> str:
        bank = Bank.get(self._bank_id)
        return bank.balance
