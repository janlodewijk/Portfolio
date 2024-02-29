from django.db import models

# Create your models here.
class bookshelf(models.Model):
    address = models.CharField(max_length=64)
    latitude = models.FloatField(max_length=64)
    longitude = models.FloatField(max_length=64)

    def __str__(self):
        return f"{self.id}. Address: {self.address} Coördinates: {self.latitude}, {self.longitude}"