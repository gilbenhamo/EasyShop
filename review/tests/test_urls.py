from django.test import SimpleTestCase
from django.urls import reverse, resolve
from review.views import commentt

class TestUrls(SimpleTestCase):
    
    def test_commentt_url(self):
        url = reverse('comment', args=['fake_id'])
        self.assertEqual(resolve(url).func, commentt)