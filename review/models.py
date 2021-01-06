from django.db import models
from account.models import Business, User
from simple_history.models import HistoricalRecords
RATE_CHOICES = [
    (1, '1 - very bad'),
    (2, '2 - bad'),
    (3, '3 - OK'),
    (4, '4 - GOOD'),
    (5, '5 - Very Good'),
]


class comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    business_comments = models.ForeignKey(Business, on_delete=models.CASCADE, default=None)
    subject = models.CharField(max_length=25)
    comment = models.TextField(max_length=255)
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES)
    date = models.DateTimeField(auto_now_add=True)
    comment_history = HistoricalRecords()

    def __str__(self):
        return '{0}-->subject {1}'.format(self.business_comments,self.subject)
