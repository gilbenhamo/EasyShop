from django.test import TestCase, Client
from django.urls import reverse, resolve
from products.models import product 
from account.models import User

class TestViews(TestCase):

    def setUp(self):
        #   Create objects
        self.client = Client()
        self.productObj = product.objects.create(
            id = 199,
            shop_id = User.objects.create(id = 199),
            product_name = 'name',
            product_info = 'info',
            product_price = 2021,
            product_amount = 10
        )

        #   Setup urls
        self.create_product_url = reverse("create_product")
        self.update_product_url = reverse("update_product",args=[199])

    def test_create_product(self):
        response = self.client.get(self.create_product_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'AddProduct.html')

    def test_update_product(self):
        response = self.client.get(self.update_product_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'updeateProduct.html')