from django.urls import path
from .views import CreateProductBulkView


app_name = 'core'

urlpatterns = [
    path('products/bulk-create/', CreateProductBulkView.as_view(), name='product-bulk-create'),
]


