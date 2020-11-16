from uuid import UUID
from bank.commands import OpenBank, RegisterCustomer, OpenAccount, DepositMoney, WithdrawMoney
from bank.queries import GetBank, GetCustomer, GetAccount
from bank.dtos import OpenBankDto, RegisterCustomerDto, OpenAccountDto, TransferMoneyDto
from bank.domain import Account, Customer, Bank


def open_bank(name: str) -> Bank:
    command = OpenBank(OpenBankDto(name))
    return command.execute()


def register_customer(bank_id: UUID, customer_name: str) -> Customer:
    command = RegisterCustomer(RegisterCustomerDto(bank_id, customer_name))
    return command.execute()


def open_account(bank_id: UUID, customer_id: UUID, account_name: str) -> Account:
    command = OpenAccount(OpenAccountDto(bank_id, customer_id, account_name))
    return command.execute()


def deposit_money(account_id: UUID, amount: int) -> Account:
    command = DepositMoney(TransferMoneyDto(account_id, amount))
    return command.execute()


def withdraw_money(account_id: UUID, amount: int) -> Account:
    command = WithdrawMoney(TransferMoneyDto(account_id, amount))
    return command.execute()


def get_bank(bank_id: UUID) -> Bank:
    query = GetBank(bank_id)
    return query.execute()


def get_customer(customer_id: UUID) -> Customer:
    query = GetCustomer(customer_id)
    return query.execute()


def get_account(account_id: UUID) -> Account:
    query = GetAccount(account_id)
    return query.execute()
