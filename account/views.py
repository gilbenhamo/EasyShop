from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from .form import User, CustomerSignUpform, BusinessSignUpform, BusinessUpdeateForm, createMassage, createDeals, \
    CATEGORY_BUSINESS, Categories
from django.contrib.auth.models import auth
from .models import Business
from products.models import product
from review.views import commentt
from cart.models import Order
from cart.views import get_user_pending_order


class customer_register(CreateView):
    model = User
    form_class = CustomerSignUpform
    template_name = 'custmer.html'

    def form_valid(self, form):  # If the registration was successful login automatically
        user = form.save()
        login(self.request, user)
        messages.info(self.request, " משתמש מסוג צרכן נוצר בהצלחה ברוך הבאה לאתר ")
        return redirect('home')


class business_register(CreateView):
    model = User
    form_class = BusinessSignUpform
    template_name = 'Business.html'

    def form_valid(self, form):  # If the registration was successful login automatically
        user = form.save()
        login(self.request, user)
        messages.info(self.request, "משתמש מסוג בעל עסק נוצר בהצלחה ברוך הבאה לאתר")
        return redirect('home')


def login_r(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:  # If the login was successful return to home page
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, "שם המתמש או הסיסמה לא נכונים")
        else:
            messages.info(request, "שם המתמש או הסיסמה לא נכונים")
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect("home")


def business_profile(request, pk_test):  # pk_test Gets a unique Id of a business profile
    get_business = Business.objects.get(user_id=pk_test)
    get_user = User.objects.get(id=pk_test)
    prods = product.objects.all()
    commentt(request, pk_test)
    if request.user.is_authenticated:
        existing_order = get_user_pending_order(request, pk_test)
    else:
        existing_order = 0
    return render(request, "business_profile.html",
                  {'prods': prods, 'get_business': get_business, 'get_user': get_user, 'order': existing_order})


@login_required
def update_business(request, pk_test): # pk_test Gets a unique Id of a business profile
    business = Business.objects.get(user_id=pk_test)
    check = int(pk_test)
    form = BusinessUpdeateForm(instance=business, )
    if request.method == 'POST':
        form = BusinessUpdeateForm(request.POST, instance=business)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user_id = request.user
            instance.save()
        return redirect('/account/business_profile/{0}/'.format(pk_test))
    context = {'form': form, 'check': check}
    return render(request, 'updeateBusiness.html', context)


def create_Massage(request, pk_test):  # pk_test Gets a unique Id of a business profile
    business = Business.objects.get(user_id=pk_test)
    form = createMassage(instance=business)
    check = int(pk_test)
    if request.method == 'POST':
        form = createMassage(request.POST, instance=business)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user_id = request.user
            instance.save()
        return redirect('/account/business_profile/{0}/'.format(pk_test))
    context = {'form': form, 'check': check}
    return render(request, 'updeateMassage.html', context)


def create_deals(request, pk_test):  # pk_test Gets a unique Id of a business profile
    business = Business.objects.get(user_id=pk_test)
    form = createDeals(instance=business)
    check = int(pk_test)
    if request.method == 'POST':
        form = createDeals(request.POST, instance=business)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user_id = request.user
            instance.save()
        return redirect('/account/business_profile/{0}/'.format(pk_test))
    context = {'form': form, 'check': check}
    return render(request, 'updateDeals.html', context)


def update_Category(request):
    if request.method == 'POST':
        categ = Categories.objects.create()
        categ.category_name = request.POST.get('Category')
        categ.save()
        CATEGORY_BUSINESS.append((len(CATEGORY_BUSINESS) + 1, request.POST.get('Category')))

    context = {'category': CATEGORY_BUSINESS}
    return render(request, 'updateCategory.html', context)


def sales_report(request):
    orders = Order.objects.filter(business_owner_id=request.user.id, status=True, customer_ready=True)
    context = {'orders': orders}
    return render(request, 'business_sales_report.html', context)


def money_report(request):
    orders = Order.objects.filter(business_owner_id=request.user.id, status=True, customer_ready=True)
    total = 0
    for o in orders:
        total += o.get_cart_total()
    context = {'orders': orders, 'total': total}
    return render(request, 'business_money_report.html', context)


def Inventory_report(request):
    prods = product.objects.filter(shop_id_id=request.user.id)
    context = {'prods': prods}
    return render(request, 'business_Inventory_report.html', context)
