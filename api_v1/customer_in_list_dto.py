from typing import NamedTuple


class CustomerInListDto(NamedTuple):
    Id: int
    Name: str
    Email: str
    MoneySpent: any
    Status: int
    StatusExpirationDate: any

    def serialize(self):
        return self._asdict()
