from django.test import TestCase,Client
from products.models import product
from account.models import User

class TestModels(TestCase):

    def setUp(self):
        #   Create objects
        self.productObj = product.objects.create(
            id = 199,
            shop_id = User.objects.create(id = 198),
            product_name = 'name',
            product_info = 'info',
            product_price = 2021,
            product_amount = 10
        )
    
    def test_product(self):
        self.assertEqual(self.productObj.id, 199)
        self.assertEqual(self.productObj.shop_id_id, 198)   # 'shop_id_id' = 'shop_id' on Data-Base
        self.assertEqual(self.productObj.product_name, 'name')
        self.assertEqual(self.productObj.product_info, 'info')
        self.assertEqual(self.productObj.product_price, 2021)
        self.assertEqual(self.productObj.product_amount, 10)
        self.assertEqual(self.productObj.__str__(), 'user: {0}-->product_name: {1}'.format(
            self.productObj.shop_id,
            self.productObj.product_name
            ))