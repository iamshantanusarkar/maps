from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response

from api.models.customer import Customer
from api.serializers.customers import CustomerSerializer

class CustomerListCreate(generics.ListCreateAPIView):

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = CustomerSerializer(queryset, many=True)
        return Response(serializer.data)

class CustomerRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    # lookup_url_kwarg = 'pk'
    # lookup_field = 'id'