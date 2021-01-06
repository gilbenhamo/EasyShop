from django.db import models
from django.contrib.auth.models import AbstractUser

from simple_history.models import HistoricalRecords


class superMassage(models.Model):
    super_Massage = models.TextField(max_length=255)
    history = HistoricalRecords()

    def __str__(self):
        return 'superMassage: {}'.format(self.super_Massage)


class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_business = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    age = models.CharField(max_length=200)

    def __str__(self):
        return 'user: {}'.format(self.user)


class Business(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    business_name = models.CharField(max_length=50)
    business_address = models.CharField(max_length=50)
    business_phone = models.CharField(max_length=10)
    business_info = models.TextField(max_length=255)
    business_category = models.CharField(max_length=50)
    business_massage = models.TextField(max_length=255)
    business_deals = models.TextField(max_length=255)

    def __str__(self):
        return 'business_name: {}'.format(self.business_name)

    def get_Business_Name(self):
        return self.business_name


class Categories(models.Model):
    category_name = models.CharField(max_length=25)

    @staticmethod
    def get_all_categories():
        return Categories.objects.all()

    def __str__(self):
        return self.category_name
