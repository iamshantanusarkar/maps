from django.db import models
from .customer import Customer
from .savedmap import SavedMap

class Favourite(models.Model):
    savedmapId = models.ForeignKey( SavedMap, on_delete=models.CASCADE, null=False, related_name="savedmap_id" )
    customerId = models.ForeignKey( Customer, on_delete=models.CASCADE, null=False, related_name="customer_id" )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'api_favourites'