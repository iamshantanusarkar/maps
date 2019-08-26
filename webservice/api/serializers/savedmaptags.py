from rest_framework import serializers
from api.models.savedmaptag import SavedMapTag

class SavedMapTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedMapTag
        fields = ('id', 'name', 'created', 'updated')