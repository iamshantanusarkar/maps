from django.shortcuts import render
from rest_framework import viewsets
from .models import SavedMap
from .serializers import SavedMapSerializer

class SavedMapView(viewsets.ModelViewSet):
    queryset = SavedMap.objects.all()
    serializer_class = SavedMapSerializer