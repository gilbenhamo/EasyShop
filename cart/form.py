from django.forms import ModelForm
from .models import Order


class createOrderComment(ModelForm):
    class Meta:
        model = Order
        fields = ['order_comments', 'customer_ready']
