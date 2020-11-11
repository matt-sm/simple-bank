from abc import ABC, abstractmethod
from domain import Bank, Customer


class DomainEvent(ABC):
    @abstractmethod
    def trigger(self) -> None:
        pass


class MoneyDeposited(DomainEvent):
    def __init__(self, bank_id: str, customer_id, amount: int) -> None:
        self._bank_id = bank_id
        self._customer_id = customer_id
        self._amount = amount

    def trigger(self) -> str:
        bank = Bank.get(self._bank_id)
        bank.deposit(self._amount)
        customer = Customer.get(self._customer_id)
        customer.deposit(self._amount)


class MoneyWithdrawn(DomainEvent):
    def __init__(self, bank_id: str, customer_id, amount: int) -> None:
        self._bank_id = bank_id
        self._customer_id = customer_id
        self._amount = amount

    def trigger(self) -> str:
        bank = Bank.get(self._bank_id)
        bank.withdraw(self._amount)
        customer = Customer.get(self._customer_id)
        customer.withdraw(self._amount)
