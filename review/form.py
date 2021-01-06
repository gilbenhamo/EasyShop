from django import forms
from review.models import comments


class RateForm(forms.ModelForm):

    class Meta:
        model = comments
        fields =['subject', 'comment', 'rate',]
