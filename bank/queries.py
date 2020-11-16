from abc import ABC, abstractmethod
from uuid import UUID
from bank.repos import BankRepo, CustomerRepo, AccountRepo
from bank.domain import Customer, Bank, Aggregate, Account
from bank.value_objects import UniqueEntityId


class Query(ABC):
    @abstractmethod
    def execute(self) -> Aggregate:
        pass


class GetCustomer(Query):
    def __init__(self, customer_id: UUID) -> None:
        self._customer_id = customer_id

    def execute(self) -> Customer:
        return CustomerRepo.findById(UniqueEntityId(self._customer_id))


class GetBank(Query):
    def __init__(self, bank_id: UUID) -> None:
        self._bank_id = bank_id

    def execute(self) -> Bank:
        return BankRepo.findById(UniqueEntityId(self._bank_id))


class GetAccount(Query):
    def __init__(self, account_id: UUID) -> None:
        self._account_id = account_id

    def execute(self) -> Account:
        return AccountRepo.findById(UniqueEntityId(self._account_id))
