from dataclasses import dataclass
from uuid import UUID


@dataclass
class OpenAccountDto:
    bank_id: UUID
    customer_id: UUID
    account_name: str


@dataclass
class TransferMoneyDto:
    account_id: UUID
    amount: int


@dataclass
class OpenBankDto:
    bank_name: str


@dataclass
class RegisterCustomerDto:
    bank_id: UUID
    customer_name: str
