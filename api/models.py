from django.db import models

# Create your models here.
from shop.models import items
    

class Login(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    usertype=models.CharField(max_length=100,default="user")


class User(models.Model):
    firstname=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    login=models.OneToOneField(Login,on_delete=models.CASCADE,related_name="login_details")


class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,related_name="cart_details",null=True)
    item=models.ForeignKey(items,on_delete=models.CASCADE,related_name="itemsincart")
    date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=30)

class Orders(models.Model):
    item=models.ForeignKey(items,on_delete=models.CASCADE,related_name="orderdetails")
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="userdetails")
    date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=100)
    

