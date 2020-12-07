from django.forms import ModelForm
from .models import product
# from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django import forms
from django.db.transaction import clean_savepoints


# CATEGORY_BUSINESS = (
#     (1, "מוצרי חשמל"),
#     (2, "מוצרים לבית"),
#     (3, "מוצרים למחשב"),
#     (4, "מוצרים לגינה"),
#     (5, "אוכל"),
# )

class createProduct(ModelForm):
    class Meta:
        model = product
        fields = ['product_name', 'product_info', 'product_price', 'product_amount' , 'product_image']  # '__all__'
