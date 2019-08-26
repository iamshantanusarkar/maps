from rest_framework import serializers
from api.models.customer import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'firstName', 'lastName', 'email', 'created', 'updated')