from apps.customers.customer import Customer
from apps.customers.models import ORMCustomer


class CustomerRepository:

    def _decode_db(self, customer):
        return Customer(name=customer.name,
                        email=customer.email,
                        id=customer.id)

    def create(self, customer):
        try:
            customer_db = ORMCustomer.objects.create(name=customer.name.value,
                                                     email=customer.email,
                                                     status=customer._status.status_type,
                                                     money_spent=customer.money_spent)
        except Exception as ex:
            raise ValueError(str(ex))
        return self._decode_db(customer_db)

    def exists_email(self, email):
        return ORMCustomer.objects.filter(email=email).exists()


