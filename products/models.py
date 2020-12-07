from django.db import models
from account.models import Business,User

# Create your models here.
class product(models.Model):
    shop_id = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    product_name = models.CharField(max_length=50)
    product_info = models.TextField(max_length=255)
    product_price = models.CharField(max_length=50)
    product_amount = models.CharField(max_length=50)
    product_image = models.ImageField(null=True, blank=True, upload_to="static/images/products_Pictures")

    def __str__(self):
        return self.product_name
    # category = models.CharField(max_length=50) optional