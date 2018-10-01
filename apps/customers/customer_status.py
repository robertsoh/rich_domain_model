from enum import Enum

from django.utils.decorators import classproperty

from apps.common.value_object import ValueObject
from apps.customers.expiration_date import ExpirationDate


class CustomerStatusType(Enum):
    Regular = 1
    Advanced = 2


class CustomerStatus(ValueObject):

    def __init__(self, status_type, expiration_date):
        if status_type not in [x.value for x in CustomerStatusType]:
            raise ValueError('El tipo de estado del cliente no es válido')
        if not expiration_date:
            raise ValueError('La fecha de expiración no debe ser nula')
        if not isinstance(expiration_date, ExpirationDate):
            raise ValueError('La fecha de expiración debe ser una instancia de ExpirationDate')

    def is_advanced(self):
        return self.status_type == CustomerStatusType.Advanced and not self.expiration_date.is_expired

    @classmethod
    def regular(cls):
        return cls(CustomerStatusType.Regular.value, ExpirationDate.infinite())
