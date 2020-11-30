from django.db import models

# Create your models here.

class user(models.Model):
    UserName= models.CharField(max_length=20)
    Password= models.CharField(max_length=16)
    LoginStatus= models.BooleanField(default=False)
    RegisterDate= models.CharField(max_length=23)
    Email= models.CharField(max_length=40)

class Custmer(user,models.Model):
    Name=models.CharField(max_length=100)
    addres=models.CharField(max_length=100)
    Phone=models.IntegerField(max_length=10)
    Age=models.IntegerField(max_length=3)
    #Mycard=class cart