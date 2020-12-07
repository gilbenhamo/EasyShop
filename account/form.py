from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms import forms, CharField
from django import forms
from .models import User, Customer, Business
from django.db.transaction import clean_savepoints
CATEGORY_BUSINESS = (
    (1, "מוצרי חשמל"),
    (2, "מוצרים לבית"),
    (3, "מוצרים למחשב"),
    (4, "מוצרים לגינה"),
    (5, "אוכל"),
)




class CustomerSignUpform(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    address = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    age = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'address', 'phone', 'age')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.username = self.cleaned_data.get('username')
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.save()
        customer = Customer.objects.create(user=user)
        customer.address = self.cleaned_data.get('address')
        customer.phone = self.cleaned_data.get('phone')
        customer.age = self.cleaned_data.get('age')
        customer.save()
        return user


class BusinessSignUpform(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    business_name = forms.CharField(required=True)
    business_address = forms.CharField(required=True)
    business_phone = forms.CharField(required=True)
    business_info = forms.CharField(required=True, widget=forms.Textarea)
    business_category = forms.TypedChoiceField(required=True, choices=CATEGORY_BUSINESS, coerce=str)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'business_name', 'business_address', 'business_phone',
                  'business_info', 'business_category')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_business = True
        user.username = self.cleaned_data.get('username')
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.save()
        business = Business.objects.create(user=user)
        business.business_name = self.cleaned_data.get('business_name')
        business.business_address = self.cleaned_data.get('business_address')
        business.business_phone = self.cleaned_data.get('business_phone')
        business.business_info = self.cleaned_data.get('business_info')
        business.business_category = self.cleaned_data.get('business_category')
        business.save()
        return user
