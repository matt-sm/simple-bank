from bank.commands import OpenBank, RegisterCustomer, OpenAccount, DepositMoney, WithdrawMoney
from bank.queries import GetAccountBalance, GetBankBalance, GetCustomerBalance


def open_bank(name: str) -> str:
    command = OpenBank(name)
    return command.execute()


def register_customer(bank_id: str, customer_name: str) -> str:
    command = RegisterCustomer(bank_id, customer_name)
    return command.execute()


def open_account(customer_id: str, account_name: str) -> str:
    command = OpenAccount(customer_id, account_name)
    return command.execute()


def deposit_money(account_id: str, amount: int) -> None:
    command = DepositMoney(account_id, amount)
    return command.execute()


def withdraw_money(account_id: str, amount: int) -> None:
    command = WithdrawMoney(account_id, amount)
    return command.execute()


def get_account_balance(account_id: str) -> int:
    query = GetAccountBalance(account_id)
    return query.execute()


def get_bank_balance(bank_id: str) -> int:
    query = GetBankBalance(bank_id)
    return query.execute()


def get_customer_balance(customer_id: str) -> int:
    query = GetCustomerBalance(customer_id)
    return query.execute()
