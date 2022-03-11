from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=40)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    author = models.CharField(max_length=40)
    description = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)
