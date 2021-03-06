from typing import NamedTuple


class CreateCustomerDto(NamedTuple):
    Name: str
    Email: str
    Id: int = None

    def serialize(self):
        return self._asdict()
