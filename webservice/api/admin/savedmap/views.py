from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response

from api.models.savedmap import SavedMap
from api.serializers.savedmaps import SavedMapSerializer

class SavedMapListCreate(generics.ListCreateAPIView):

    queryset = SavedMap.objects.all()
    serializer_class = SavedMapSerializer

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = SavedMapSerializer(queryset, many=True)
        return Response(serializer.data)

class SavedMapRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = SavedMapSerializer
    queryset = SavedMap.objects.all()
    # lookup_url_kwarg = 'pk'
    # lookup_field = 'id'