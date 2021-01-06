from django.db import models
from account.models import Business, User
from products.models import product
from django.utils import timezone


class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    ordered = models.BooleanField(default=False)
    product = models.ForeignKey(product, on_delete=models.SET_NULL, null=True)
    date_added = models.DateTimeField(auto_now=True)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.product.product_name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    business_owner = models.ForeignKey(User, related_name='%(class)s_buisness', on_delete=models.CASCADE, default=None)
    products = models.ManyToManyField(OrderItem)
    status = models.BooleanField(default=False)
    order_type = models.BooleanField(default=False)
    customer_ready = models.BooleanField(default=False)
    order_comments = models.CharField(max_length=255, default="no additional comments")

    def get_cart_items(self):
        return self.products.all()

    def get_order_date(self):
        prods = self.products.all()
        if len(prods):
            return prods[0].date_added
        return timezone.now()

    def get_cart_total(self):
        return sum([prod.product.product_price * prod.quantity for prod in self.products.all()])

    def __str__(self):
        return 'Business:{0} --> Customer: {1}'.format(self.business_owner, self.user)

    def is_ready(self):
        return self.status

    def is_take_away(self):
        return self.order_type

    def is_customer_ready(self):
        return self.customer_ready

    def get_busi_name(self):
        b = Business.objects.get(user_id=self.business_owner)
        return b.business_name

    def get_cart_amount(self):
        return sum([prod.quantity for prod in self.products.all()])
