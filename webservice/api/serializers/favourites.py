from rest_framework import serializers
from api.models.favourite import Favourite

class FavouriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favourite
        fields = ('id', 'created', 'updated')