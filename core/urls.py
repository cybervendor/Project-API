from django.urls import path
from .views import CreateProductAPIView, CreateVariantAPIView
from .views import createProductBULKAPIView, createVariantBULKAPIView


app_name = 'core'
urlpatterns = [

    path('products/', CreateProductAPIView.as_view(), name='create_product'),
    path('variants/', CreateVariantAPIView.as_view(), name='create_variant'),
    path('products/bulk/', createProductBULKAPIView.as_view(), name='create_bulk_product'),
    path('variants/bulk/',createVariantBULKAPIView.as_view(), name='create_bulk_variant')
    
]

