from abc import ABC, abstractmethod
from bank.domain import Bank, Customer
from bank.value_objects import Amount


class DomainEvent(ABC):
    @abstractmethod
    def trigger(self) -> None:
        pass


class MoneyDeposited(DomainEvent):
    def __init__(self, bank_id: str, customer_id: str, amount: Amount) -> None:
        self._bank_id = bank_id
        self._customer_id = customer_id
        self._amount = amount

    def trigger(self) -> str:
        bank = Bank.get(self._bank_id)
        customer = Customer.get(self._customer_id)
        bank.balance += self._amount
        customer.balance += self._amount
        bank.save()
        customer.save()


class MoneyWithdrawn(DomainEvent):
    def __init__(self, bank_id: str, customer_id: str, amount: Amount) -> None:
        self._bank_id = bank_id
        self._customer_id = customer_id
        self._amount = amount

    def trigger(self) -> str:
        bank = Bank.get(self._bank_id)
        customer = Customer.get(self._customer_id)
        bank.balance -= self._amount
        customer.balance -= self._amount
        bank.save()
        customer.save()
