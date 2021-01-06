from django.db import models
from account.models import User


class feedbackBox(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    feedback_subject = models.CharField(max_length=50)
    feedback_info = models.TextField(max_length=255)

    def __str__(self):
        return 'feedback_subject: {}'.format(self.feedback_subject)
