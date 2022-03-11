from rest_framework import serializers
from products import models


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = "__all__"


class ProductSingleImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductImage
        fields = ['id', 'image']


class ProductDetailsSerializer(serializers.ModelSerializer):
    productimage_set = ProductSingleImageSerializer(many=True)

    class Meta:
        ordering = ['-id']
        model = models.Product
        fields = ['id', 'name', 'price', 'author', 'description', 'time_created', 'productimage_set']


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductImage
        fields = "__all__"
