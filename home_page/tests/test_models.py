from django.test import TestCase
from home_page.models import feedbackBox
from account.models import User

class TestModels(TestCase):
    
    def setUp(self):
        #   Create an object
        self.feedback = feedbackBox.objects.create(
            name = User.objects.create(),
            feedback_subject = 'Subject',
            feedback_info = 'Info'
        )
    #   Test
    def test_feedback(self):
        self.assertEqual(self.feedback.feedback_subject, 'Subject')
        self.assertEqual(self.feedback.feedback_info, 'Info')
