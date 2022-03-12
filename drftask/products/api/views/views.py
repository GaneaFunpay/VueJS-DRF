from rest_framework import generics, status, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from products import models
from products.api import serializers


class ProductPagination(PageNumberPagination):
    page_size = 2


class ProductListView(viewsets.ModelViewSet):
    queryset = models.Product.objects.all().order_by('id')
    serializer_class = serializers.ProductDetailsSerializer
    pagination_class = ProductPagination


class ProductCreateView(APIView):
    def post(self, request, *args, **kwargs):
        product_serializer = serializers.ProductSerializer(data=request.data)
        if product_serializer.is_valid(raise_exception=True):
            _product = product_serializer.save()
            photos_data = [
                {
                    'product': _product.id,
                    'image': image
                }
                for image in self.request.FILES.getlist('images')
            ]
            images_serializer = serializers.ProductImageSerializer(data=photos_data, many=True)
            if images_serializer.is_valid(raise_exception=True):
                images_serializer.save()
        return Response(serializers.ProductDetailsSerializer(_product).data, status=status.HTTP_201_CREATED)


class ProductRetrieveView(generics.RetrieveAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductDetailsSerializer


class ProductUpdateView(generics.UpdateAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer


class ProductDeleteView(generics.DestroyAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer


class ProductImageDeleteView(generics.DestroyAPIView):
    queryset = models.ProductImage.objects.all()
    serializer_class = serializers.ProductImageSerializer

    def perform_destroy(self, instance):
        instance.image.delete(save=True)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductImageCreateView(generics.CreateAPIView):
    queryset = models.ProductImage.objects.all()
    serializer_class = serializers.ProductImageSerializer
