from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.views.generic import CreateView
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
import psycopg2
from django.contrib import messages
from django.shortcuts import render, redirect
from .form import User, CustomerSignUpform, BusinessSignUpform , BusinessUpdeateForm
from django.contrib.auth.models import auth
from .models import Business
from products.models import product


class customer_register(CreateView):
    model = User
    form_class = CustomerSignUpform
    template_name = 'custmer.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class business_register(CreateView):
    model = User
    form_class = BusinessSignUpform
    template_name = 'Business.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


def login_r(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect("home")


def business_profile(request, pk_test):
    get_business = Business.objects.get(user_id=pk_test)
    get_user = User.objects.get(id=pk_test)
    prods = product.objects.all()
    return render(request, "business_profile.html",
                  {'prods': prods, 'get_business': get_business, 'get_user': get_user})


def update_business(request, pk_test):
    business = Business.objects.get(user_id=pk_test)
    form = BusinessUpdeateForm(instance=business,)
    if request.method == 'POST':
        form = BusinessUpdeateForm(request.POST, instance=business)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user_id = request.user
            instance.save()
        return redirect('/account/business_profile/{0}/'.format(pk_test))
    context = {'form': form}
    return render(request, 'updeateBusiness.html', context)
