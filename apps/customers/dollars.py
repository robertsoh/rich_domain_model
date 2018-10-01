from decimal import Decimal

from apps.common.result import Result
from apps.common.value_object import ValueObject


class Dollars(ValueObject):

    MAX_DOLLAR_AMOUNT = Decimal(1000000)

    def __init__(self, value):
        if not isinstance(value, Decimal):
            raise TypeError('El cantidad debe ser una instancia de Decimal')
        if value < 0:
            raise ValueError('La cantidad no puede ser negativa')
        if value > self.MAX_DOLLAR_AMOUNT:
            raise ValueError('La cantidad no puede ser más grande que {}'.format(self.MAX_DOLLAR_AMOUNT))

    def is_zero(self):
        return self.value == 0

    @classmethod
    def create(cls, amount):
        try:
            return Result.ok(cls(amount))
        except Exception as ex:
            return Result.fail({'money_spent':  [str(ex)]})

