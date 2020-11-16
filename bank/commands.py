from abc import ABC, abstractmethod
from bank.domain import Bank, Customer, Account, Aggregate
from bank.events import MoneyDeposited, MoneyWithdrawn
from bank.value_objects import Amount, UniqueEntityId, Name
from bank.dtos import OpenAccountDto, TransferMoneyDto, RegisterCustomerDto, OpenBankDto
from bank.repos import AccountRepo, CustomerRepo, BankRepo


class InvalidName(Exception):
    pass


class Command(ABC):
    @abstractmethod
    def execute(self) -> Aggregate:
        pass


class OpenBank(Command):
    def __init__(self, request: OpenBankDto) -> None:
        self._request = request

    def execute(self) -> Bank:
        bank = Bank(Name(self._request.bank_name))
        BankRepo.save(bank)
        return bank


class RegisterCustomer(Command):
    def __init__(self, request: RegisterCustomerDto) -> None:
        self._request = request

    def execute(self) -> Customer:
        customer = Customer(UniqueEntityId(self._request.bank_id), Name(self._request.customer_name))
        CustomerRepo.save(customer)
        return customer


class OpenAccount(Command):
    def __init__(self, request: OpenAccountDto) -> None:
        self._request = request

    def execute(self) -> Account:
        account = Account(
            UniqueEntityId(self._request.bank_id),
            UniqueEntityId(self._request.customer_id),
            Name(self._request.account_name),
        )
        AccountRepo.save(account)
        return account


class DepositMoney(Command):
    def __init__(self, request: TransferMoneyDto) -> None:
        self._request = request

    def execute(self) -> Account:
        account = AccountRepo.findById(UniqueEntityId(self._request.account_id))
        account.deposit(Amount(self._request.amount))

        event = MoneyDeposited(account.bank_id, account.customer_id, Amount(self._request.amount))
        event.trigger()
        return account


class WithdrawMoney(Command):
    def __init__(self, request: TransferMoneyDto) -> None:
        self._request = request

    def execute(self) -> Account:
        account = AccountRepo.findById(UniqueEntityId(self._request.account_id))
        account.withdraw(Amount(self._request.amount))

        event = MoneyWithdrawn(account.bank_id, account.customer_id, Amount(self._request.amount))
        event.trigger()
        return account
