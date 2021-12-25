from typing import TypeGuard
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.db.models.fields.files import ImageField

# Create your models here.

class Customerdetail(models.Model):
    user=models.OneToOneField(User,null=True,blank=True,on_delete=CASCADE)
    name=models.CharField(max_length=50,null=True)
    profilepic=models.ImageField(null=True,blank=True,default='profileimage.jpg')
    email=models.EmailField(max_length=100,null=True)
    contactnumber=models.CharField(max_length=25,null=True,blank=True,default='update contact')
    address=models.CharField(max_length=500,null=True,blank=True,default='update address')
    dateofcreated=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    productname=models.CharField(max_length=50,null=True,blank=True)
    productmenupic=models.ImageField(null=True,blank=True,default='profileimage.jpg')
    productbuypic1=models.ImageField(null=True,blank=True,default='profileimage.jpg')
    productbuypic2=models.ImageField(null=True,blank=True,default='profileimage.jpg')
    productbuypic3=models.ImageField(null=True,blank=True,default='profileimage.jpg')
    productprice=models.FloatField(null=True,blank=True)
    offerprice=models.FloatField(null=True,blank=True)
    quantity=models.IntegerField(null=True,blank=True)
    soiltype=models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.productname

class Cart(models.Model):
    name=models.CharField(max_length=50,null=True,blank=True)
    user=models.ForeignKey(User,null=True,blank=True,on_delete=CASCADE)
    product=models.ForeignKey(Product,null=True,blank=True,on_delete=CASCADE)

    def __str__(self):
        return self.name 

class Order(models.Model):
    productname=models.CharField(max_length=50,null=True,blank=True)
    name=models.CharField(max_length=25,null=True,blank=True)
    user=models.ForeignKey(User,null=True,blank=True,on_delete=CASCADE)
    product=models.ForeignKey(Product,null=True,blank=True,on_delete=CASCADE)
    address=models.CharField(max_length=500,null=True,blank=True)
    contactnumber=models.CharField(max_length=10,null=True,blank=True)
    orderstatus=models.CharField(max_length=25,null=True,blank=True,default="order placed")
    ordereddate=models.DateTimeField(auto_now_add=True,null=True)
    paymentmode=models.CharField(max_length=25,null=True,blank=True)

    def __str__(self):
        return self.productname 
