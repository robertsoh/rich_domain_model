from datetime import datetime

from apps.common.value_object import ValueObject
# from simple_value_object import ValueObject


class ExpirationDate(ValueObject):

    def __init__(self, date):
        if date is not None and not isinstance(date, datetime):
            raise TypeError('Tipo inválido: La fecha debe ser un objeto datetime')

    @staticmethod
    def infinite(cls):
        return cls(None)

    def is_expired(self):
        return self.date < datetime.now()
