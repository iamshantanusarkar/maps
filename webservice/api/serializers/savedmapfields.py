from rest_framework import serializers
from api.models.savedmapfield import SavedMapField

class SavedMapFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedMapField
        fields = ('id', 'created', 'updated')