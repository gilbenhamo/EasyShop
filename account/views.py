from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.views.generic import CreateView
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
import psycopg2
from django.contrib import messages
from django.shortcuts import render, redirect
from .form import User, CustomerSignUpform, BusinessSignUpform, BusinessUpdeateForm, createMassage, createDeals ,CATEGORY_BUSINESS,createCategories,Categories
from django.contrib.auth.models import auth
from .models import Business
from products.models import product
from review.views import commentt

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
    commentt(request, pk_test)
    return render(request, "business_profile.html",
                  {'prods': prods, 'get_business': get_business, 'get_user': get_user})


@login_required
def update_business(request, pk_test):
    business = Business.objects.get(user_id=pk_test)
    check=int(pk_test)
    print(check)
    form = BusinessUpdeateForm(instance=business, )
    if request.method == 'POST':
        form = BusinessUpdeateForm(request.POST, instance=business)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user_id = request.user
            instance.save()
        return redirect('/account/business_profile/{0}/'.format(pk_test))
    context = {'form': form,'check':check}
    return render(request, 'updeateBusiness.html', context)


def create_Massage(request, pk_test):
    business = Business.objects.get(user_id=pk_test)
    form = createMassage(instance=business)
    check=int(pk_test)
    print(check)
    if request.method == 'POST':
        form = createMassage(request.POST, instance=business)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user_id = request.user
            instance.save()
        return redirect('/account/business_profile/{0}/'.format(pk_test))
    context = {'form': form,'check':check}
    return render(request, 'updeateMassage.html', context)


def create_deals(request, pk_test):
    business = Business.objects.get(user_id=pk_test)
    form = createDeals(instance=business)
    check=int(pk_test)
    print(check)
    if request.method == 'POST':
        form = createDeals(request.POST, instance=business)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user_id = request.user
            instance.save()
        return redirect('/account/business_profile/{0}/'.format(pk_test))
    context = {'form': form,'check':check}
    return render(request, 'updateDeals.html', context)

def update_Category(request):
    # form = createCategories()
    # if request.method == 'POST':
    #     form = createCategories(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         print(form)
    #         CATEGORY_BUSINESS.append((len(CATEGORY_BUSINESS)+1,form.category_name))
    #     return redirect('home')
    if request.method == 'POST':
        categ = Categories.objects.create()
        categ.category_name=request.POST.get('Category')
        categ.save()
        CATEGORY_BUSINESS.append((len(CATEGORY_BUSINESS) + 1,request.POST.get('Category')))

    context = {'category': CATEGORY_BUSINESS}
    return render(request,'updateCategory.html',context)