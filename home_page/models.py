from django.db import models


# Create your models here.
class users_Easy(models.Model):
    name = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    nickName = models.CharField(max_length=20)
    password = models.CharField(max_length=18)


class Super(models.Model):
    name = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    nickName = models.CharField(max_length=20)
    password = models.CharField(max_length=18)

