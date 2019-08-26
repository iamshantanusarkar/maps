from django.db import models
from .savedmap import SavedMap
from .tag import Tag

class SavedMapTag(models.Model):
    savedmap = models.ForeignKey( SavedMap, on_delete=models.CASCADE, null=False, related_name="savedmap_id" )
    tag = models.ForeignKey( Tag, on_delete=models.CASCADE, null=False, related_name="tag_id" )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'api_saved_map_tags'