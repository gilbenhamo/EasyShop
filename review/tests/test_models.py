from django.test import TestCase,Client
from review.models import comments, RATE_CHOICES
from account.models import User, Business

class TestModels(TestCase):

    def setUp(self):
        #   Create objects
        self.commentObj = comments.objects.create(
            user = User.objects.create(id = 199),
            business_comments = Business.objects.create(user = User.objects.get(id = 199),),
            subject = 'sub',
            comment = 'com',
            rate = 3
        )
    
    def test_comments(self):
        self.assertEqual(self.commentObj.user.id, 199)
        self.assertEqual(self.commentObj.business_comments.user.id, 199)
        self.assertEqual(self.commentObj.subject, 'sub')
        self.assertEqual(self.commentObj.comment, 'com')
        self.assertEqual(self.commentObj.rate, 3)
        self.assertEqual(self.commentObj.__str__(), '{0}-->subject {1}'.format(
            self.commentObj.business_comments,
            self.commentObj.subject
            ))
    
    def test_RATE_CHOICES(self):
        self.assertEqual(RATE_CHOICES[0], (1, '1 - very bad'))
        self.assertEqual(RATE_CHOICES[1], (2, '2 - bad'))
        self.assertEqual(RATE_CHOICES[2], (3, '3 - OK'))
        self.assertEqual(RATE_CHOICES[3], (4, '4 - GOOD'))
        self.assertEqual(RATE_CHOICES[4], (5, '5 - Very Good'))