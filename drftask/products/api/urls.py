from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers

from products.api.views import views


router = routers.DefaultRouter()
router.register('product', views.ProductListView, basename="product")

urlpatterns = [
    path('', include(router.urls)),
    path('product_create', views.ProductCreateView.as_view()),
    path('product_detail/<int:pk>', views.ProductRetrieveView.as_view()),
    path('product_update/<int:pk>', views.ProductUpdateView.as_view()),
    path('product_delete/<int:pk>', views.ProductDeleteView.as_view()),
    path('image_delete/<int:pk>', views.ProductImageDeleteView.as_view()),
    path('image_create', views.ProductImageCreateView.as_view()),
]
