from django.test import TestCase
from home_page.form import create_feedback

class TestForms(TestCase):

    def test_create_feedback_is_valid(self):
        form = create_feedback(data={})
        self.assertFalse(form.is_valid())   #This form is emptey
        self.assertEqual(len(form.errors),2)
      




