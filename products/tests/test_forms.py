from django.test import TestCase
from products.form import createProduct

class TestForms(TestCase):

    def test_createPrpdict_no_data(self):
        form = createProduct(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors),4)