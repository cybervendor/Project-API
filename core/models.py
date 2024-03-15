from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Variant(models.Model):
    name = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name= 'variants')
    
    def __str__(self):
        return f"{self.name} - {self.product.name}"
