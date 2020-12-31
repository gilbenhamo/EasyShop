from django.forms import ModelForm
from .models import Order
# from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django import forms
from django.db.transaction import clean_savepoints


class createOrderComment(ModelForm):
    class Meta:
        model = Order
        fields = ['order_comments','customer_ready']