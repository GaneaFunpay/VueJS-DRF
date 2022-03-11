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
        product_serializer = serializers.ProductSerializer(data=self.request.data)
        if product_serializer.is_valid():
            _product = product_serializer.save()
            for image in self.request.FILES.getlist('images'):
                product_image = serializers.ProductImageSerializer(
                    data={
                        'product': _product.id,
                        'image': image
                    }
                )
                if product_image.is_valid():
                    product_image.save()
                else:
                    return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
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
        print('abobapidor')
        instance.image.delete(save=True)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductImageCreateView(generics.CreateAPIView):
    queryset = models.ProductImage.objects.all()
    serializer_class = serializers.ProductImageSerializer
