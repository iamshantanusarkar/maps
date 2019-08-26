from django.db import models
from .customer import Customer

class SavedMap(models.Model):
    name = models.CharField(max_length=50)
    customer = models.ForeignKey( Customer, on_delete=models.CASCADE, null=False, related_name="customer_id" )
    numberOfViews = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'api_saved_maps'