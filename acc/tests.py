from django.test import TestCase, Client, SimpleTestCase
from django.urls import reverse, resolve
from acc.views import Business, custmer, logout, login
import json
class TestUrls(SimpleTestCase):

    def test_customer_url_is_resolved(self):
        url = reverse('custmer')
        print(resolve(url))
        self.assertEqual(resolve(url).func, custmer)

    def test_business_url_is_resolved(self):
        url = reverse('Business')
        print(resolve(url))
        self.assertEqual(resolve(url).func, Business)


    def test_login_url_is_resolved(self):
        url = reverse('login')
        print(resolve(url))
        self.assertEqual(resolve(url).func, login)

    def test_logout_url_is_resolved(self):
        url = reverse('logout')
        print(resolve(url))
        self.assertEqual(resolve(url).func, logout)

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.custmer_url = reverse('custmer')
        self.Business_url = reverse('Business')
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')

    def test_custmer(self):
        response = self.client.get(self.custmer_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'custmer.html')

    def Business(self):
        response = self.client.get(self.Business_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Business.html')

    def login(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def logout(self):
        response = self.client.get(self.logout_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'logout.html')

# Create your tests here.
