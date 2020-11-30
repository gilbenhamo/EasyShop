from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.

# class baseUser(AbstractBaseUser):
#     username = models.CharField(max_length=255)  # add max_length=255,blank=True,null=True
#     full_name = models.CharField(max_length=255, blank=True, null=True)
#     email = models.EmailField(max_length=255, unique=True)
#     active = models.BooleanField(default=True)
#     staff = models.BooleanField(default=False)
#     admin = models.BooleanField(default=False)
#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['full_name']
#
#     def __str__(self):
#         return self.username
#
#     def get_ful_name(self):
#         return self.username
#
#     def get_short_name(self):
#         return self.username
#
#     @property
#     def is_staff(self):
#         return self.staff
#
#     @property
#     def is_admin(self):
#         return self.admin
#
#     @property
#     def is_active(self):
#         return self.active
#
#
# class BusinessOwner(models.Model):
#     NameBusiness = models.CharField(max_length=100)
#     Category = models.CharField(max_length=100)
#     addres = models.CharField(max_length=100)
#     Phone = models.CharField(max_length=10)
