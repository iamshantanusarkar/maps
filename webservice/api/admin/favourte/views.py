from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response

from api.models.favourite import Favourite
from api.serializers.favourites import FavouriteSerializer

class FavouriteListCreate(generics.ListCreateAPIView):

    queryset = Favourite.objects.all()
    serializer_class = FavouriteSerializer

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = FavouriteSerializer(queryset, many=True)
        return Response(serializer.data)

class FavouriteRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = FavouriteSerializer
    queryset = Favourite.objects.all()
    # lookup_url_kwarg = 'pk'
    # lookup_field = 'id'