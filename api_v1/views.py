from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from api_v1.create_customer_dto import CreateCustomerDto
from api_v1.customer_in_list_dto import CustomerInListDto
from apps.common.decorators import serialize_exceptions
from apps.customers.customer import Customer
from apps.customers.customer_name import CustomerName
from apps.customers.repository import CustomerRepository


class CustomerListCreateAPIView(APIView):

    def __init__(self, *args, **kwargs):
        self._customer_repository = CustomerRepository()
        super().__init__(*args, **kwargs)

    @serialize_exceptions
    def post(self, request, *args, **kwargs):
        customer_dto = CreateCustomerDto(Name=request.data.get('Name'),
                                         Email=request.data.get('Email'))
        customer_name_or_error = CustomerName.create(customer_dto.Name)
        if customer_name_or_error.is_failure:
            raise ValidationError(customer_name_or_error.error)
        if self._customer_repository.check_if_email_exists(customer_dto.Email):
            raise ValidationError(
                {'email': 'El correo {} ya se encuentra en uso'.format(customer_dto.Email)}
            )
        customer = Customer(name=customer_name_or_error.value, email=customer_dto.Email)
        customer = self._customer_repository.create(customer)
        customer_dto = CreateCustomerDto(Id=customer.id,
                                         Name=customer.name.value,
                                         Email=customer.email)
        return Response(customer_dto.serialize(), status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        customers = self._customer_repository.get_all_customers()
        customers_dtos = []
        for customer in customers:
            customer_dto = CustomerInListDto(Id=customer.id,
                                             Name=customer.name.value,
                                             Email=customer.email,
                                             MoneySpent=customer.money_spent,
                                             Status=customer.status.status_type,
                                             StatusExpirationDate=customer.status.expiration_date.date)
            customers_dtos.append(customer_dto.serialize())
        return Response(customers_dtos)
