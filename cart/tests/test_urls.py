from django.test import SimpleTestCase
from django.urls import reverse, resolve
from cart.views import show_cart, show_orders, history_orders

class TestUrls(SimpleTestCase):

    def test_show_cart_url_is_resolved(self):
        url = reverse('show_cart', args=['fake_id_1'])
        self.assertEqual(resolve(url).func, show_cart)

    def test_show_orders_url(self):
        url = reverse('show_orders', args=['fake_id_2'])
        self.assertEqual(resolve(url).func, show_orders)

    def test_history_orders_url(self):
        url = reverse('history_orders', args=['fake_id_3'])
        self.assertEqual(resolve(url).func, history_orders)