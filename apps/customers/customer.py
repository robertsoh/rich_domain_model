from apps.customers.customer_status import CustomerStatus


class Customer(object):

    def __init__(self, name, email):
        if not name:
            raise ValueError('El nombre no puede ser nulo')
        if not email:
            raise ValueError('El correo no puede ser nulo')
        self._name = name
        self._email = email
        self._money_spent = 0
        self._status = CustomerStatus.regular

