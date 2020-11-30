from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class baseUserManager(BaseUserManager):
    def create_user(self, email, full_name, password=None, is_active=True, is_staff=False, is_admin=False):
        if not password:
            raise ValueError("User must have an password")
        if not full_name:
            raise ValueError("User must have an full_name")
        if not email:
            raise ValueError("User must have an email")
        user_obj = self.model(
            email=self.normalize_email(email)
        )
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        #user_obj.username = username
        user_obj.full_name = full_name
        user_obj.set_password(password)  # how to change password
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, full_name, password=None):
        user = self.create_user(
            email,
            full_name,
            password=password,
            is_staff=True
        )
        return user

    def create_superuser(self, email, full_name, password=None):
        user = self.create_user(
            email,
            full_name,
            password=password,
            is_staff=True,
            is_admin=True
        )
        return user

    def create_customer(self, email, full_name, password, address, phone, age):
        user = self.create_user(
            email,
            full_name,
            password=password,
            is_staff=True,
            is_admin=True
        )
        user.address = address
        user.phone = phone
        user.age = age
        return user

    def create_business(self, email, full_name, password, address, phone, Category, BusinessName):
        user = self.create_user(
            email,
            full_name,
            password=password,
            is_staff=True,
            is_admin=True
        )
        user.BusinessName = BusinessName
        user.Category = Category
        user.address = address
        user.phone = phone

        return user


class baseUser(AbstractBaseUser):
    #username = models.CharField(max_length=255)  # add max_length=255,blank=True,null=True
    full_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, unique=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']  # must to input

    object = baseUserManager()  # make user object

    def __str__(self):
        return self.email

    def get_ful_name(self):
        if self.full_name:
            return self.full_name
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active


class Customer(models.Model):
    user = models.OneToOneField(baseUser, on_delete=models.CASCADE)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    age = models.CharField(max_length=200)

class BusinessOwner(models.Model):
    user = models.OneToOneField(baseUser, on_delete=models.CASCADE)
    BusinessName = models.CharField(max_length=100)
    Category = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    Phone = models.CharField(max_length=10)


