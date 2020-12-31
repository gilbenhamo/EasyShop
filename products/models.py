from django.db import models
from django.shortcuts import redirect
from django.urls import reverse

from account.models import Business,User,Customer

# Create your models here.
class product(models.Model):
    shop_id = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    product_name = models.CharField(max_length=50)
    product_info = models.TextField(max_length=255)
    product_price = models.IntegerField()
    product_amount = models.IntegerField()
    product_image = models.ImageField(null=True, blank=True, upload_to="static/images/products_Pictures")

    def __str__(self):
        return 'user: {0}-->product_name{1}'.format(self.shop_id,self.product_name)
    # category = models.CharField(max_length=50) optional

    # def get_add_to_cart_url(self):
    #     return reverse('cart:add-to-cart',kwargs={'id':self.id})