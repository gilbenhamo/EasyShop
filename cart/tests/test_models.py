from django.test import TestCase,Client
from cart.models import OrderItem, Order
from account.models import User
from products.models import product

class TestModels(TestCase):

    def setUp(self):
        #  Create objects
        self.productObj = product.objects.create(
            id = 199,
            shop_id = User.objects.create(id = 198),
            product_name = 'name',
            product_info = 'info',
            product_price = 2021,
            product_amount = 10
        )
        self.orderItemObj = OrderItem.objects.create(
            user = User.objects.create(id = 197, username = 'SpongBob'),
            product = self.productObj
        )

        self.orderObj = Order.objects.create(
            user = User.objects.create(id = 196, username = 'MrCrab'),
            business_owner = User.objects.get(id = 196),
            order_comments = 'Comment-spam'
        )

    def test_OrderItem(self):
        self.assertEqual(self.orderItemObj.user.id, 197)
        self.assertEqual(self.orderItemObj.product.id, 199)
        self.assertTrue(self.orderItemObj.quantity == 1)    # Default
        self.assertFalse(self.orderItemObj.ordered)         # Default
        self.assertEqual(self.orderItemObj.__str__(), self.orderItemObj.product.product_name)

    def test_Order(self):
        self.assertEqual(self.orderObj.user.id, 196)
        self.assertEqual(self.orderObj.business_owner.id, 196)
        self.assertFalse(self.orderObj.status)                  # Default
        self.assertFalse(self.orderObj.order_type)              # Default
        self.assertFalse(self.orderObj.customer_ready)          # Default
        self.assertEqual(self.orderObj.order_comments, 'Comment-spam')
        self.assertEqual(self.orderObj.__str__(), 'Business:{0} --> Customer: {1}'.format(self.orderObj.business_owner, self.orderObj.user))
        self.assertEqual(self.orderObj.get_cart_total(), 0)     # Default
        self.assertFalse(self.orderObj.is_ready())              # Default
        self.assertFalse(self.orderObj.is_customer_ready())     # Default
        self.assertFalse(self.orderObj.is_take_away())          # Default
        self.assertEqual(self.orderObj.get_cart_amount(), 0)    # Default