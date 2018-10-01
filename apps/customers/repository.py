from apps.customers.customer import Customer
from apps.customers.customer_name import CustomerName
from apps.customers.customer_status import CustomerStatus
from apps.customers.expiration_date import ExpirationDate
from apps.customers.models import ORMCustomer


class CustomerRepository:

    def _decode_db(self, db_customer):
        customer = Customer(id=db_customer.id,
                            name=CustomerName(db_customer.name),
                            email=db_customer.email)
        customer._status = CustomerStatus(db_customer.status,
                                          ExpirationDate(db_customer.status_expiration_date))
        customer._money_spent = db_customer.money_spent
        return customer

    def create(self, customer):
        try:
            db_customer = ORMCustomer.objects.create(name=customer.name.value,
                                                     email=customer.email,
                                                     money_spent=customer.money_spent,
                                                     status=customer._status.status_type,
                                                     status_expiration_date=customer._status.expiration_date.date)
        except Exception as ex:
            raise ValueError(str(ex))
        return self._decode_db(db_customer)

    def check_if_email_exists(self, email):
        return ORMCustomer.objects.filter(email=email).exists()

    def get_all_customers(self):
        db_customers = ORMCustomer.objects.all()
        customers = []
        for db_customer in db_customers:
            customers.append(self._decode_db(db_customer))
        return customers
