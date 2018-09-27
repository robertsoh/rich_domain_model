from apps.common.result import Result
from apps.common.value_object import ValueObject


class CustomerName(ValueObject):

    def __init__(self, value):
        value = value or ''
        if not value:
            raise ValueError('El nombre del cliente no puede ser vacío')
        if len(value) > 100:
            raise ValueError('El nombre del cliente es muy largo')

    @classmethod
    def create(cls, customer_name):
        try:
            return Result.ok(cls(customer_name))
        except Exception as ex:
            return Result.fail({'name':  [str(ex)]})
