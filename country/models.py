from django.db import models

# Create your models here.
class Country(models.Model):
    country_name = models.CharField(max_length=100)
    population = models.BigIntegerField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.country_name
    