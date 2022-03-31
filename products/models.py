from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    inventory_quanity = models.IntegerField()