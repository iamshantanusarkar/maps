from django.db import models

class Customer(models.Model):
    title = models.CharField(max_length=50)
    firstName = models.CharField(max_length=50)
    middleName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'api_customers'
    
    def __unicode__(self):
        return '%d: %s' % (self.firstName, self.lastName)