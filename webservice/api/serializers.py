from rest_framework import serializers
from .models import SavedMap

class SavedMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedMap
        fields = ('id', 'name', 'slug', 'created', 'updated')