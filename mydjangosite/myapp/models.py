from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class  Login(models.Model):
    #LOGIN_ID = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    username=models.CharField(max_length=50, null=True)
    password=models.CharField(max_length=50, null=True)
    # usertype=models.CharField(max_length=50)
class Category(models.Model):
    name=models.CharField(max_length=50, null =True)
    image=models.CharField(max_length=200, default="")
    # def _str_(self):
    #       return self.cat_name
class Product(models.Model):
    name=models.CharField(max_length=50)
    rate =models.CharField(max_length=50)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    CATEGORY_ID = models.ForeignKey(Category, on_delete=models.CASCADE)
   # SHOP_ID = models.ForeignKey(shops, on_delete=models.CASCADE, default=1)
    def _str_(self):
          return self.product_name

class Buyer(models.Model):
    f_name=models.CharField(max_length=50, null=True)
    l_name=models.CharField(max_length=50, null=True)
    phone=models.CharField(max_length=50, null=True)
    email= models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=50, null=True)
    town= models.CharField(max_length=50,default="", null=True)
    # county= models.CharField(max_length=50,default="", null=True)
    zipcode = models.CharField(max_length=50, null=True)
    # image= models.CharField(max_length=100)
    LOGIN_ID = models.OneToOneField(Login, on_delete=models.CASCADE, default=1)
    def _str_(self):
          return self.name

class Cart(models.Model):
    quantity = models.CharField(max_length=50, null=True)
    total_amt = models.FloatField(max_length=50, null=True)
    PRODUCT_ID = models.ForeignKey(Product, on_delete=models.CASCADE)
    Buyer_ID = models.ForeignKey(Buyer, on_delete=models.CASCADE)

class Shipping_address(models.Model):
    f_name = models.CharField(max_length=50, null=True)
    l_name = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=50, null=True)
    town = models.CharField(max_length=50, null=True)
    zipcode = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=50, null=True)
    LOGIN_ID = models.OneToOneField(Login, on_delete=models.CASCADE, default=1)

class Bank(models.Model):
    card_no = models.CharField(max_length=50, null=True)
    cardholder_name = models.CharField(max_length=50, null=True)
    expiration = models.CharField(max_length=50, null=True)
    cvv = models.CharField(max_length=50, null=True)
    balance = models.CharField(max_length=50, null=True)

