from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers

from products.api.views import views

router = routers.DefaultRouter()
router.register('api/v1/product', views.ProductListView, basename="api/v1/product")



urlpatterns = [
    path('', include(router.urls)),
    path('api/v1/product_create', views.ProductCreateView.as_view()),
    path('api/v1/product_detail/<int:pk>', views.ProductRetrieveView.as_view()),
    path('api/v1/product_update/<int:pk>', views.ProductUpdateView.as_view()),
    path('api/v1/product_delete/<int:pk>', views.ProductDeleteView.as_view()),
    path('api/v1/image_delete/<int:pk>', views.ProductImageDeleteView.as_view()),
    path('api/v1/image_create', views.ProductImageCreateView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
