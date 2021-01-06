from django.test import TestCase, Client
from django.urls import reverse
from review.models import comments
from account.models import User, Business

class TestViews(TestCase):

    '''Login required - cant test all functunals'''
    def setUp(self):
        # Create objects
        self.client = Client()
        self.commentObj = comments.objects.create(
            user = User.objects.create(id = 199),
            business_comments = Business.objects.create(user = User.objects.get(id = 199),),
            subject = 'subject-spam',
            comment = 'comment-spam',
            rate = 3
        )

    def test_commentt(self):
        # Check if user and business_comments are the same
        self.assertEqual(
            self.commentObj.user,
            self.commentObj.business_comments.user
            )

