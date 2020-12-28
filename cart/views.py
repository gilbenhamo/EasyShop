from django.shortcuts import render
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic import ListView, DetailView, View
from .models import Order, OrderItem
from products.models import product
from account.models import Customer
from account.models import Business
from django.urls import reverse
from account.models import User

def get_user_pending_order(request,busi_id):
    # get order for the correct user
    #user_profile = get_object_or_404(User, user=request.user)
    user = request.user
    order = Order.objects.filter(user=user,business_owner=busi_id,status=False)
    if order.exists():
        # get the only order in the list of filtered orders
        return order[0]
    return 0

def add_to_cart(request, **kwargs):
    user = request.user
    # business = Business.objects.get(user_id=kwargs.get('pk_test'))
    products = product.objects.filter(id=kwargs.get('item_id', "")).first()
    order_item, status = OrderItem.objects.get_or_create(product=products)
    user_order, status = Order.objects.get_or_create(user=user, business_owner=products.shop_id, status=False)
    # user_order.business_owner = business
    user_order.products.add(order_item)
    user_order.save()
    return redirect(reverse('home'))


def show_cart(request, busi_id,):
    existing_order = get_user_pending_order(request,busi_id)
    context = {
        'order': existing_order,
    }
    return render(request, 'cart.html', context)
