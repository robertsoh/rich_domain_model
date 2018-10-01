from apps.customers.customer_name import CustomerName
from apps.customers.customer_status import CustomerStatus


class Customer(object):

    def __init__(self, name, email, id=None):
        self._name = name
        self._email = email
        self._money_spent = 0
        self._status = CustomerStatus.regular()
        self._id = id

    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email

    @property
    def status(self):
        return self._status

    @property
    def money_spent(self):
        return self._money_spent

    @property
    def id(self):
        return self._id
