from django.db import models

# Create your models here.
class ConsoleCategory(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Console(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=999)
    category = models.ForeignKey(ConsoleCategory, on_delete=models.CASCADE)
    company = models.CharField(max_length=255)
    price = models.FloatField()

    def __str__(self):
        return self.name

class ConsoleImage(models.Model):
    image = models.CharField(max_length=999)
    console = models.ForeignKey(Console, on_delete=models.CASCADE)
    image2 = models.CharField(max_length=999)
    image3 = models.CharField(max_length=999)
    image4 = models.CharField(max_length=999)
