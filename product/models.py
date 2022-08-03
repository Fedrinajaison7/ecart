from django.db import models
from numpy import average, product

class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    @property
    def get_category_total(self):
        category_products = self.product_set.all()
        total = sum([product.price for product in category_products])
        return total
    
    @property
    def get_category_avg(self):
        category_products = self.product_set.all()
        total_avg = average([product.price for product in category_products])
        return total_avg
    
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField() 
    photo = models.ImageField(blank = False)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    