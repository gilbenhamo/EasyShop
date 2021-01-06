from django.test import SimpleTestCase
from django.urls import reverse, resolve
from account.views import login_r, logout, sales_report, money_report, Inventory_report, sales_report, update_business, update_Category, business_profile, create_deals, create_Massage
from cart.views import add_to_cart, remove_from_cart, business_report

class TestUrls(SimpleTestCase):
    
    def test_login_r_url_is_resolved(self):
        url = reverse('login_r')
        self.assertEqual(resolve(url).func, login_r)

    def test_logout_url_is_resolved(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func, logout)

    def test_business_profile_url_is_resolved(self):
        url = reverse('business_profile', args = ['fake_id'])
        self.assertEqual(resolve(url).func, business_profile)

    def test_update_business_is_resolved(self):
        url = reverse('update_business', args = ['fake_id'])
        self.assertEqual(resolve(url).func, update_business)

    def test_create_Massage_url_is_resolved(self):
        url = reverse('create_Massage', args = ['fake_id'])
        self.assertEqual(resolve(url).func, create_Massage)

    def test_create_deals_is_resolved(self):
        url = reverse('create_deals', args = ['fake_id'])
        self.assertEqual(resolve(url).func, create_deals)

    def test_update_Category_is_resolved(self):
        url = reverse('update_Category')
        self.assertEqual(resolve(url).func, update_Category)

    def test_add_to_cart_url_is_resolved(self):
        url = reverse('add_to_cart', args = ['fake_id'])
        self.assertEqual(resolve(url).func, add_to_cart)

    def test_remove_from_cart_is_resolved(self):
        url = reverse('remove_from_cart', args = ['fake_id'])
        self.assertEqual(resolve(url).func, remove_from_cart)

    def test_business_report_is_resolved(self):
        url = reverse('business_report')
        self.assertEqual(resolve(url).func, business_report)

    def test_sales_report_is_resolved(self):
        url = reverse('sales_report')
        self.assertEqual(resolve(url).func, sales_report)

    def test_money_report_is_resolved(self):
        url = reverse('money_report')
        self.assertEqual(resolve(url).func, money_report)

    def test_Inventory_report_is_resolved(self):
        url = reverse('Inventory_report')
        self.assertEqual(resolve(url).func, Inventory_report)