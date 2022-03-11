from django.db import models
from .product import Product


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.FileField(blank=False, null=False, upload_to='product')

    def __str__(self):
        return "{} : {}".format(self.product.name, self.image.name)
