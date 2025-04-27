from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    address = models.CharField(max_length=500, blank=True) 
    province = models.CharField(max_length=100, blank=True) 
    post_code = models.CharField(max_length=5, blank=True)
    tel = models.CharField(max_length=20, blank=True)
    fullname = models.CharField(max_length=255, blank=True, null=True)

class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField()
    stock = models.IntegerField()
    category = models.CharField(max_length=255)

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.CharField(max_length=500)

class Shipping(models.Model):
    method = models.CharField(max_length=255)
    fee = models.FloatField()

class Payment(models.Model):
    payment_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    method = models.CharField(max_length=255)
    card_no = models.CharField(max_length=255)
    expired = models.CharField(max_length=5)
    holder_name = models.CharField(max_length=500)

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.FloatField()
    status = models.CharField(max_length=50)
    shipping = models.ForeignKey(Shipping, on_delete=models.SET_NULL, null=True)
    payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, null=True)

class ProductOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    total_price = models.FloatField()
    quantity = models.IntegerField()

# Create your models here.

