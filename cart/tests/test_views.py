from django.test import TestCase, Client
from django.urls import reverse, resolve
from products.models import product
from account.models import User, Business
from cart.models import Order

class TestViews(TestCase):

    def setUp(self):
        #   Create objects
        self.client = Client()
        self.UserObj = User.objects.create(
            is_customer = True,
            is_business = False,
            first_name = 'Jim',
            last_name = 'Botten'
        )
        self.BusinessObj = Business.objects.create(
            user = self.UserObj,
            business_name = 'Zoglovek',
            business_address = 'Hash',
            business_phone = '0528847793',
            business_info = 'info_info',
            business_category = 'Naknikim',
            business_massage = 'Special message',
            business_deals = 'Special deal',
        )

        #   Setup urls
        self.show_orders_url = reverse('show_orders', args=[self.BusinessObj.user_id])
        self.history_orders_url = reverse('history_orders', args=[self.BusinessObj.user_id])

    def test_show_orders(self):
        response = self.client.get(self.show_orders_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'showOrders.html')

    def test_history_orders(self):
        response = self.client.get(self.history_orders_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'history_orders.html')
