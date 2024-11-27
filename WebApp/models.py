from django.db import models


class ContactDB(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Mobile = models.CharField(max_length=100, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Message = models.TextField(max_length=200, null=True, blank=True)


class SignupDB(models.Model):
    Signup_Name = models.CharField(max_length=100, null=True, blank=True)
    Signup_Email = models.EmailField(max_length=100, null=True, blank=True)
    Signup_Mobile = models.CharField(max_length=100, null=True, blank=True)
    Signup_Password = models.CharField(max_length=100, null=True, blank=True)
    Signup_ConfirmPassword = models.CharField(max_length=100, null=True, blank=True)


class CartDB(models.Model):
    Username = models.CharField(max_length=100, null=True, blank=True)
    Product_Name = models.CharField(max_length=100, null=True, blank=True)
    Product_Quantity = models.IntegerField(null=True, blank=True)
    Total_Price = models.IntegerField(null=True, blank=True)
    Product_Image = models.ImageField(upload_to="cart_images/", null=True, blank=True)


class OrderDB(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Place = models.CharField(max_length=100, null=True, blank=True)
    Address = models.CharField(max_length=100, null=True, blank=True)
    Mobile = models.IntegerField(null=True, blank=True)
    Message = models.CharField(max_length=100, null=True, blank=True)
    TotalPrice = models.IntegerField(null=True, blank=True)
