from rest_framework import serializers
from .models import Product, Variant


class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = 'Variant'
        fields = ('price','name')
        
class ProductSerializer(serializers.ModelSerializer):
    variants = VariantSerializer(many=True)
    
    class Meta:
        model = Product
        fields = ('id', 'name','variants')