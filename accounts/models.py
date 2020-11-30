from django.db import models


# Create your models here.

class user(models.Model):
    UserName= models.CharField(max_length=20)
    Password= models.CharField(max_length=16)
    Email= models.CharField(max_length=40)


class BusinessOwner(models.Model):
    UserName= models.CharField(max_length=20)
    Password= models.CharField(max_length=16)
    Email= models.CharField(max_length=40)
    NameBusiness=models.CharField(max_length=100)
    Category=models.CharField(max_length=100)
    addres=models.CharField(max_length=100)
    Phone=models.CharField(max_length=10)



