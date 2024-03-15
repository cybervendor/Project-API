from .models import Product, Variant
from rest_framework import generics, status
from .serializers import ProductSerializer, VariantSerializer
from rest_framework.response import Response

# Create your views here.

class CreateProductAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CreateVariantAPIView(generics.CreateAPIView):
    queryset = Variant.objects.all()
    serializer_class = VariantSerializer

class createProductBULKAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def POST(self, request):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        if serializer.is_valid():
            products_data = serializer.validated_data
            products = [Product(**item) for item in products_data]
            Product.objects.bulk_create(products)
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class createVariantBULKAPIView(generics.CreateAPIView):
    queryset = Variant.objects.all()
    serializer_class = VariantSerializer
    
    def POST(self, request):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        if serializer.is_valid():
            variants_data = serializer.validated_data
            variants = [Variant(**item) for item in variants_data]
            Variant.objects.bulk_create(variants)
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


