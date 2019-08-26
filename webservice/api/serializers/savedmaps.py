from rest_framework import serializers
from api.models.savedmap import SavedMap
from api.serializers.customers import CustomerSerializer

class SavedMapSerializer(serializers.ModelSerializer):

    customer_id = CustomerSerializer(many=False)

    class Meta:
        model = SavedMap
        fields = ('id', 'name', 'customer_id', 'numberOfViews', 'created', 'updated')