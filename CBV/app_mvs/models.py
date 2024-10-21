from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    cupdatedAt = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    
class Supplier(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(null=True,blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    cupdatedAt = models.DateTimeField(auto_now=True)   
    
    def __str__(self):
        return self.name 
    
class Products(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    cupdatedAt = models.DateTimeField(auto_now=True) 
    category = models.ForeignKey(Category,related_name='product_category',on_delete=models.CASCADE)       
    supplier = models.ManyToManyField(Supplier,related_name='product_category')       