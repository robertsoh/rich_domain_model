from rest_framework import serializers


class CreateCustomerSerializer(serializers.Serializer):

    name = serializers.CharField()
    email = serializers.EmailField()
    id = serializers.IntegerField(read_only=True)

    @staticmethod
    def serialize(customer):
        data = {
            'id': customer.id,
            'name': customer.name.value,
            'email': customer.email
        }
        return data
