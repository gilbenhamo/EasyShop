from django.conf import settings
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from accounts.models import BusinessOwner, user


class BusinessUserBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        user = self.getUser(username)
        if user is None:
            return None
        pwd_valid = check_password(password, user.password)
        if pwd_valid:
            return user
        return None

    def getUser(self, username):
        try:
            return BusinessOwner.objects.get(UserName=username)
        except:
            return None
