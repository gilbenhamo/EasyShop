from django.db import models
from account.models import Business

# Create your models here.
class product(models.Model):
    product_name = models.CharField(max_length=50)
    product_info = models.TextField(max_length=255)
    product_price = models.CharField(max_length=50)
    product_amount = models.CharField(max_length=50)
    #product_image = models.ImageField(upload_to="static/images/products_Pictures", height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.product_name
    # category = models.CharField(max_length=50) optional