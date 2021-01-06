from django.shortcuts import render, redirect
from .form import createProduct
from django.http import HttpResponse
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

