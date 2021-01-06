from django.test import TestCase
from account.form import CustomerSignUpform, BusinessSignUpform, createCategories, BusinessUpdeateForm, createDeals, createMassage

class TestForms(TestCase):

    def test_CustomerSignUpform_no_data(self):
        form = CustomerSignUpform(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors),8)


    def test_create_BusinessSignUpform_no_data(self):
        form = BusinessSignUpform(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors),10)

    def test_BusinessUpdeateForm_no_data(self):
        form = BusinessUpdeateForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors),5)

    def test_createMassage_no_data(self):
        form = createMassage(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors),1)

    def test_createDeals_no_data(self):
        form = createDeals(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors),1)

    def test_createCategories_no_data(self):
        form = createCategories(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors),1)

    