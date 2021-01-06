from django.forms import ModelForm
from .models import product


class createProduct(ModelForm):
    class Meta:
        model = product
        fields = ['product_name', 'product_info', 'product_price', 'product_amount', 'product_image']  # '__all__'
