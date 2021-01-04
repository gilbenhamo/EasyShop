from django.test import TestCase, Client, SimpleTestCase
from django.urls import reverse, resolve
from home_page.views import home, Abutus, Registar, feedback, searchByCategory, search, adminReports
from cart.views import customer_orders


class TestUrls(SimpleTestCase):

    def test_home_url_is_resolved(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, home)

    def test_Abutus_url_is_resolved(self):
        url = reverse('AbutUs')
        self.assertEqual(resolve(url).func, Abutus)

    def test_Registar_url_is_resolved(self):
        url = reverse('Registar')
        self.assertEqual(resolve(url).func, Registar)

    def test_feedback_url_is_resolved(self):
        url = reverse('feedback')
        self.assertEqual(resolve(url).func, feedback)

    def test_searchByCategory_url_is_resolved(self):
        url = reverse('searchByCategory', args=['fake_category'])
        self.assertEqual(resolve(url).func, searchByCategory)

    def test_search_url_is_resolved(self):
        url = reverse('search')
        self.assertEqual(resolve(url).func, search)

    def test_admin_reports_url_is_resolved(self):
        url = reverse('admin_reports')
        self.assertEqual(resolve(url).func, adminReports)

    def test_customer_orders_url_is_resolved(self):
        url = reverse('customer_orders')
        self.assertEqual(resolve(url).func, customer_orders)
