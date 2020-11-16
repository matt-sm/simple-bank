from abc import ABC, abstractmethod
from bank.repos import BankRepo, CustomerRepo
from bank.value_objects import Amount, UniqueEntityId


class DomainEvent(ABC):
    @abstractmethod
    def trigger(self) -> None:
        pass


class MoneyDeposited(DomainEvent):
    def __init__(self, bank_id: UniqueEntityId, customer_id: UniqueEntityId, amount: Amount) -> None:
        self._bank_id = bank_id
        self._customer_id = customer_id
        self._amount = amount

    def trigger(self) -> None:
        bank = BankRepo.findById(self._bank_id)
        customer = CustomerRepo.findById(self._customer_id)

        customer.increase_balance(self._amount)
        bank.increase_balance(self._amount)

        CustomerRepo.save(customer)
        BankRepo.save(bank)


class MoneyWithdrawn(DomainEvent):
    def __init__(self, bank_id: UniqueEntityId, customer_id: UniqueEntityId, amount: Amount) -> None:
        self._bank_id = bank_id
        self._customer_id = customer_id
        self._amount = amount

    def trigger(self) -> None:
        bank = BankRepo.findById(self._bank_id)
        customer = CustomerRepo.findById(self._customer_id)
        customer.decrease_balance(self._amount)
        bank.decrease_balance(self._amount)

        CustomerRepo.save(customer)
        BankRepo.save(bank)
