from django.forms import ModelForm
from .models import feedbackBox


class create_feedback(ModelForm):
    class Meta:
        model = feedbackBox
        fields = ['feedback_subject', 'feedback_info']
