from django.db import models
from account.models import Business, Customer, User
from products.models import product
from simple_history.models import HistoricalRecords


# Create your models here.


class OrderItem(models.Model):
    product = models.OneToOneField(product, on_delete=models.SET_NULL, null=True)
    date_added = models.DateTimeField(auto_now=True)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.product.product_name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    business_owner = models.ForeignKey(User,related_name='%(class)s_buisness', on_delete=models.CASCADE, default=None)
    products = models.ManyToManyField(OrderItem)
    status = models.BooleanField(default=False)
    order_type = models.BooleanField(default=False)
    customer_ready = models.BooleanField(default=False)

    def get_cart_items(self):
        return self.products.all()

    def get_cart_total(self):
        return sum([prod.product.product_price for prod in self.products.all()])

    def __str__(self):
        return '{0} - {1}'.format(self.status, self.user)

    def is_ready(self):
        return self.status

    def is_take_away(self):
        return self.order_type

    def is_customer_ready(self):
        return self.customer_ready
