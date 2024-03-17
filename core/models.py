from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='product_images/', null=True)
    
    def __str__(self):
        return self.name
    
class ProductVariant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name= 'variants')
    sku = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    details = models.TextField()
    
    
    def __str__(self):
        return f"{self.name} - {self.product.name}"
