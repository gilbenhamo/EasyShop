from django.test import TestCase
from review.form import RateForm

class TestForms(TestCase):

    def test_RateForm_no_data(self):
        form = RateForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),3)