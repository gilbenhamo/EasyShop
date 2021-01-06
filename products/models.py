from django.db import models


from account.models import User

class product(models.Model):
    shop_id = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    product_name = models.CharField(max_length=50)
    product_info = models.TextField(max_length=255)
    product_price = models.IntegerField()
    product_amount = models.IntegerField()
    product_image = models.ImageField(null=True, blank=True, upload_to="static/images/products_Pictures")

    def __str__(self):
        return 'user: {0}-->product_name: {1}'.format(self.shop_id,self.product_name)