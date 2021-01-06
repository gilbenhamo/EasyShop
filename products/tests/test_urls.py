from django.test import SimpleTestCase
from django.urls import reverse, resolve
from products.views import update_product, create_product

class TestUrls(SimpleTestCase):
    
    def test_create_product_url_is_resolved(self):
        url = reverse('create_product')
        self.assertEqual(resolve(url).func, create_product)

    def test_update_product_url_is_resolved(self):
        url = reverse('update_product', args = ['fake_id'])
        self.assertEqual(resolve(url).func, update_product)