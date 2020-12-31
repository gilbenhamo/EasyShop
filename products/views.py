from django.shortcuts import render, redirect
from .models import product
from .form import createProduct
from django.views.generic import CreateView
from account.models import User, Business
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import Permission
# from .decorators import allowed_users
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .models import *
from django.contrib import messages


def create_product(request):
    if User.is_business:
        form = createProduct()
        if request.method == 'POST':
            form = createProduct(request.POST, request.FILES)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.shop_id = request.user
                instance.save()
                messages.info(request, "המוצר נוסף בהצלחה")
            return redirect('/account/business_profile/{0}/'.format(request.user.id))

        context = {'form': form}
        return render(request, 'AddProduct.html', context)
    else:
        return HttpResponse('Access un-authorized')


def update_product(request, pk_test):
    prod = product.objects.get(id=pk_test)
    form = createProduct(instance=prod)
    if request.method == 'POST':
        form = createProduct(request.POST,request.FILES, instance=prod)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.shop_id = request.user
            instance.save()
        return redirect('/account/business_profile/{0}/'.format(request.user.id))

    context = {'form': form}
    return render(request, 'updeateProduct.html', context)


def createOrder(request,pk):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=10)
    customer = Customer.objects.get(user_id=pk)
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)
    # form = OrderForm(initial={'customer':customer})
    if request.method == 'POST':
        # print('Printing POST:', request.POST)
        # form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    context = {'form': formset}
    return render(request, 'order_form.html', context)