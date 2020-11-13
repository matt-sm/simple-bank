from dataclasses import dataclass


class InvalidNameError(Exception):
    pass


@dataclass(frozen=True)
class Name:
    name: str

    def __post_init__(self):
        if len(self.name) == 0:
            raise InvalidNameError