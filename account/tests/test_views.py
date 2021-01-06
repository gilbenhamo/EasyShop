from django.test import TestCase, Client
from django.urls import reverse, resolve
from account.models import Business, User

class TestViews(TestCase):

    def setUp(self):
        #   Create objects
        self.client = Client()
        self.business_object_test = Business.objects.create(user = User.objects.create(id = 199))

        #   Setup urls   
        self.login_r_url = reverse("login_r")
        self.business_profile_url = reverse("business_profile", args=[199])
        self.create_Massage_url = reverse("create_Massage", args=[199])
        self.create_deals_url = reverse("create_deals", args=[199])
        self.update_Category_url = reverse("update_Category")
        self.business_report_url = reverse("business_report")
        self.sales_report_url = reverse("sales_report")
        self.money_report_url = reverse("money_report")
        self.Inventory_report_url = reverse("Inventory_report")

    def test_login_r(self):
        response = self.client.get(self.login_r_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_business_profile(self):
        response = self.client.get(self.business_profile_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'business_profile.html')

    def test_create_Massage(self):
        response = self.client.get(self.create_Massage_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'updeateMassage.html')

    def test_create_deals(self):
        response = self.client.get(self.create_deals_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'updateDeals.html')

    def test_update_Category(self):
        response = self.client.get(self.update_Category_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'updateCategory.html')

    def test_business_report(self):
        response = self.client.get(self.business_report_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'business_report.html')

    def test_sales_report(self):
        response = self.client.get(self.sales_report_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'business_sales_report.html')

    def test_money_report(self):
        response = self.client.get(self.money_report_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'business_money_report.html')

    def test_Inventory_report(self):
        response = self.client.get(self.Inventory_report_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'business_Inventory_report.html')