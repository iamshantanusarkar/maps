from django.db import models

class SavedMap(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
