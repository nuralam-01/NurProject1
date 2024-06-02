from mailbox import Message
from django import db
from django.db import models

# Create your models here.
#for CONTACT
class Contact(models.Model):
    Your_name = models.CharField(max_length=20)
    Email = models.EmailField(max_length=20)
    Subject = models.CharField(max_length=20)     
    Message = models.TextField()
    class Meta:
        db_table = 'Contact'
 #For product details
class AddProduct(models.Model):
   Pid = models.IntegerField(primary_key=True)
   Pname = models.CharField(max_length=20)
   quantity = models.IntegerField()
   costPrice = models.IntegerField()
   sale = models.IntegerField()
   Description= models.TextField(blank=True, null=True)
   Pimg = models.ImageField(upload_to ='img/',blank=True,null=True )
   class Meta:
       db_table = 'AddProduct'
 
#For Sign up/ Sign in 
class Users(models.Model):
    Name = models.TextField()
    Email = models.EmailField(primary_key=True)
    Password = models.TextField()
    class Meta:
        db_table = 'Users'
        
#For Cart
class Cartitem(models.Model):
    Cartid = models.IntegerField(primary_key=True)
    Product = models.ForeignKey(AddProduct,on_delete=models.CASCADE)
    Quantity = models.PositiveIntegerField(default=0)
    User = models.ForeignKey(Users,on_delete=models.CASCADE)
    Date_added = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'Cartitem'

        
#For Orders
class Order(models.Model):
    Ordername = models.IntegerField(primary_key=True)
    Userid = models.ForeignKey(Users,on_delete=models.SET_NULL,null=True)
    DateofOrder = models.DateTimeField()
    Product = models.ForeignKey(AddProduct,on_delete=models.SET_NULL,null=True)
    Quantity = models.IntegerField()
    Totalammount = models.IntegerField()
    CompleteTrans = models.BooleanField()
    class Meta:
        db_table = 'Order'
    
  
    