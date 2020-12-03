from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_business = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    # email = models.EmailField(max_length=255, unique=True)


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    age = models.CharField(max_length=200)


class Business(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    business_name = models.CharField(max_length=50)
    business_address = models.CharField(max_length=50)
    business_phone = models.CharField(max_length=10)
    business_info = models.TextField(max_length=255)
    business_category = models.CharField(max_length=50)
