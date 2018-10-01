from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from api_v1.serializers import CreateCustomerSerializer
from apps.common.decorators import serialize_exceptions
from apps.customers.customer import Customer
from apps.customers.customer_name import CustomerName
from apps.customers.repository import CustomerRepository


class CreateCustomerAPIView(APIView):

    def __init__(self, *args, **kwargs):
        self._customer_repository = CustomerRepository()
        super().__init__(*args, **kwargs)

    @serialize_exceptions
    def post(self, request, *args, **kwargs):
        serializer = CreateCustomerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        customer_name_or_error = CustomerName.create(serializer.validated_data.get('name'))
        if customer_name_or_error.is_failure:
            raise ValidationError(customer_name_or_error.error)
        if self._customer_repository.exists_email(serializer.validated_data.get('email')):
            raise ValidationError(
                {'email': 'El correo {} ya se encuentra en uso'.format(serializer.validated_data.get('email'))}
            )
        customer = Customer(name=customer_name_or_error, email=serializer.validated_data.get('email'))
        customer_db = self._customer_repository.create(customer)
        return Response(CreateCustomerSerializer.serialize(customer_db), status=status.HTTP_201_CREATED)
