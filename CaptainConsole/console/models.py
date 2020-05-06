from django.db import models

# Create your models here.
class ConsoleCategory(models.Model):
    name = models.CharField(max_length=255)

class Console(models.Model):
    name = models.CharField(max_length=255),
    description = models.CharField(max_length=999),
    category = models.ForeignKey(ConsoleCategory, on_delete=models.CASCADE),
    company = models.CharField(max_length=255),
    price = models.FloatField()
