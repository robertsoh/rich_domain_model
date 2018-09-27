from datetime import datetime

from django.utils.decorators import classproperty

from apps.common.result import Result
from apps.common.value_object import ValueObject


class ExpirationDate(ValueObject):

    def __init__(self, date):
        if date is not None and not isinstance(date, datetime):
            raise TypeError('Tipo inválido: La fecha debe ser un objeto datetime')

    @classmethod
    def infinite(cls):
        return cls(None)

    @classmethod
    def create(cls, date):
        try:
            return Result.ok(cls(date))
        except Exception as ex:
            return Result.fail({'status_expiration_date':  [str(ex)]})

    def is_expired(self):
        return self != ExpirationDate.infinite() and self.date < datetime.now()
