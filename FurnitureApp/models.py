from django.db import models


class CategoryDB(models.Model):
    Category_Name = models.CharField(max_length=100, null=True, blank=True)
    Category_Description = models.TextField(max_length=200, null=True, blank=True)
    Category_Image = models.ImageField(upload_to="category_images", null=True, blank=True)


class ProductDB(models.Model):
    Product_Category = models.CharField(max_length=100, null=True, blank=True)
    Product_Name = models.CharField(max_length=100, null=True, blank=True)
    Product_Quantity = models.IntegerField(null=True, blank=True)
    Product_MRP = models.IntegerField(null=True, blank=True)
    Product_Description = models.TextField(max_length=300, null=True, blank=True)
    Product_Country = models.CharField(max_length=100, null=True, blank=True)
    Product_Mfd = models.CharField(max_length=100, null=True, blank=True)
    up = models.ImageField(upload_to='product_images/', null=True, blank=True)
    Product_Image2 = models.ImageField(upload_to='product_images/', null=True, blank=True)
    Product_Image3 = models.ImageField(upload_to='product_images/', null=True, blank=True)
