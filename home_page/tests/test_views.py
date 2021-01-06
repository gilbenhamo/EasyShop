from django.test import TestCase, Client, SimpleTestCase
from django.urls import reverse, resolve
from home_page.views import feedback, home, Abutus, Registar, search, adminReports, searchByCategory

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()  #Create a client object
        
        #   Setup urls
        self.home_url = reverse('home')
        self.abutUs_url = reverse('AbutUs')
        self.Registar_url = reverse('Registar')
        self.feedback_url = reverse('feedback')
        self.search_url = reverse('search')
        self.adminReports_url = reverse('admin_reports')

    #   Tests
    def test_home(self):
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_Abutus(self):
        response = self.client.get(self.abutUs_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'abutUs.html')

    def test_Registar(self):
        response = self.client.get(self.Registar_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Registar.html')

    def test_feedback(self):
        response = self.client.get(self.feedback_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'feedback.html')

    def test_search(self):
        response = self.client.get(self.search_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search.html')

    def test_adminReports(self):
        response = self.client.get(self.adminReports_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin_reports.html')


