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
from .form import createOrderComment


def get_user_pending_order(request, busi_id):
    # get order for the correct user
    user = request.user
    order = Order.objects.filter(user=user, business_owner=busi_id, customer_ready=False)
    if order.exists():
        # get the only order in the list of filtered orders
        return order[0]
    return 0


def add_to_cart(request, **kwargs):
    user = request.user
    products = get_object_or_404(product, id=kwargs.get('item_id', ""))
    order_item, status= OrderItem.objects.get_or_create(product_id = kwargs.get('item_id', ""), user = user, ordered=False)
    user_order = Order.objects.filter(user=user, business_owner=products.shop_id, customer_ready=False)
    if user_order.exists():
        order = user_order[0]
        # Add amount to order item
        if order.products.filter(product_id = products.id).exists():
            order_item.quantity += 1
            order_item.save()
        else:
            order.products.add(order_item)
            
    else:
        order = Order.objects.create(business_owner=products.shop_id, user = user)
        order.products.add(order_item)
    messages.info(request, "המוצר נוסף לעגלה")
    return redirect('/account/business_profile/{0}/'.format(products.shop_id_id))

def remove_from_cart(request, **kwargs):
    user = request.user
    products = get_object_or_404(product, id=kwargs.get('item_id', ""))
    user_order = Order.objects.filter(user= user, business_owner=products.shop_id, customer_ready=False)
    if user_order.exists():
        order = user_order[0]
        # Remove
        if order.products.filter(product_id = products.id).exists():
            order_item = OrderItem.objects.filter(product_id = kwargs.get('item_id', ""), user = user, ordered=False)[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
                messages.info(request, "המוצר הוסר מהעגלה")
            else:
                order.products.remove(order_item)
                messages.info(request, "אין אפשרות להוריד מוצר שלא קיים בעגלה")
        else:
            # Add a massage "user dont have any items in the cart"
            messages.info(request, "אין אפשרות להוריד מוצר שלא קיים בעגלה")
            return redirect('/account/business_profile/{0}/'.format(products.shop_id_id))
    else:
        # Add a massage "There is no order"
        return redirect('/account/business_profile/{0}/'.format(products.shop_id_id))
    return redirect('/account/business_profile/{0}/'.format(products.shop_id_id))


def show_cart(request, busi_id):
    existing_order = get_user_pending_order(request, busi_id)
    get_business = Business.objects.get(user_id=busi_id)
    context = {
        'order': existing_order,
        'get_business': get_business,
    }
    if request.method == 'POST':
        user = request.user
        order = Order.objects.filter(user=user, business_owner=busi_id, customer_ready=False).update(customer_ready=True, order_comments = request.POST.get('comment'))
        for orde in existing_order.get_cart_items():
            element = product.objects.get(id = orde.product_id)
            OrderItem.objects.filter(user = user).update(ordered = True)
            prod = product.objects.filter(shop_id = busi_id, id = orde.product_id).update(product_amount = element.product_amount - orde.quantity)

        return redirect('/account/business_profile/{0}/'.format(busi_id))
    return render(request, 'cart.html', context)

# def ready_customer_orders(request,busi_id):
#     if request.method == 'POST':
#         user = request.user
#         order_ready = Order.objects.filter(user=user,status=True)
#         print(order_ready)
#         order_not_ready = Order.objects.filter(user=user, status=False)
#         context = {'order_ready': order_ready, 'order_not_ready': order_not_ready}
#     return render(request, 'customer_orders.html', context)

def show_orders(request, busi_id):
    orders = Order.objects.all()
    context = {'orders':orders, 'business':busi_id}
    return render(request, 'showOrders.html', context)

def history_orders(request, busi_id):
    orders = Order.objects.filter(business_owner=busi_id, status=True)
    context = {'orders':orders, 'business':busi_id}
    return render(request, 'history_orders.html', context)