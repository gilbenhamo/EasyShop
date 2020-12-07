from django.test import TestCase, Client, SimpleTestCase
from django.urls import reverse, resolve
from home_page.views import home, Abutus, Registar
import json

class TestUrls(SimpleTestCase):

    def test_home_url_is_resolved(self):
        url = reverse('home')
        print(resolve(url))
        self.assertEqual(resolve(url).func, home)

    def test_Abutus_url_is_resolved(self):
        url = reverse('AbutUs')
        print(resolve(url))
        self.assertEqual(resolve(url).func, Abutus)


    def test_Registar_url_is_resolved(self):
        url = reverse('Registar')
        print(resolve(url))
        self.assertEqual(resolve(url).func, Registar)

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')
        self.abutUs_url = reverse('AbutUs')
        self.Registar_url = reverse('Registar')

    def test_custmer(self):
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def Business(self):
        response = self.client.get(self.abutUs_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'abutUs.html')

    def login(self):
        response = self.client.get(self.Registar_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Registar.html')

# Create your tests here.
