from dataclasses import dataclass, field
import uuid


class InvalidNameError(Exception):
    pass


class InvalidAmountError(Exception):
    pass


@dataclass(frozen=True)
class Name:
    value: str

    def __post_init__(self):
        if len(self.value) == 0:
            raise InvalidNameError


@dataclass(frozen=True)
class Amount:
    value: float

    def __post_init__(self):
        if self.value < 0:
            raise InvalidAmountError

    def __add__(self, other):
        return Amount(self.value + other.value)

    def __sub__(self, other):
        if other.value <= self.value:
            return Amount(self.value - other.value)
        raise InvalidAmountError

    def __ge__(self, other):
        return self.value >= other.value


@dataclass(frozen=True)
class UniqueEntityId:
    value: str = uuid.uuid1()
