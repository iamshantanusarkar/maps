from django.db import models
from .savedmap import SavedMap

class SavedMapField(models.Model):
    savedmap = models.ForeignKey( SavedMap, on_delete=models.CASCADE, null=False, related_name="savedmap_id" )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'api_saved_map_fields'