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


# Create your views here.
# @allowed_users(allowed_roles=['is_business'])
# @permission_required('product.create_product')

def create_product(request):
    if User.is_business:
        form = createProduct()
        if request.method == 'POST':
            form = createProduct(request.POST, request.FILES)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.shop_id = request.user
                instance.save()
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

# def prod_pass(request):
#     prods = product.objects.all()
#
#     return render(request, "business_profile.html", {'prods': prods})
