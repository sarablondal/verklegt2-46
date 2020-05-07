from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=255)

class Account(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    zipCode = models.IntegerField()
    phoneNumber = models.IntegerField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)


