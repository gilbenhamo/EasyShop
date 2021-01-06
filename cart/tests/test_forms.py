from django.test import TestCase
from cart.form import createOrderComment

class TestForms(TestCase):

    def test_createOrderComment_no_data(self):
        form = createOrderComment(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors),1)