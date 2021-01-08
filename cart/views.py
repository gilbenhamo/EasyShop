from django.contrib import messages
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from .models import Order, OrderItem
from products.models import product
from account.models import Business


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
    products = get_object_or_404(product, id=kwargs.get('item_id', ""))  # Get a unique product ID in the store
    order_item, status = OrderItem.objects.get_or_create(product_id=kwargs.get('item_id', ""), user=user, ordered=False)
    user_order = Order.objects.filter(user=user, business_owner=products.shop_id, customer_ready=False)
    if (products.product_amount > 0):  # Checks that the product is in stock
        if user_order.exists():
            order = user_order[0]
            # Add amount to order item
            if order.products.filter(product_id=products.id).exists():
                if order_item.quantity < products.product_amount:  # Make sure the consumer does not order more than
                    # the existing stock
                    order_item.quantity += 1
                    order_item.save()
                    messages.info(request, "המוצר נוסף לעגלה")
                else:
                    messages.info(request, "אין אפשרות להוסיף עוד כל המלאי הקיים בעגלה שלך")
            else:
                order.products.add(order_item)  # Adds to a product that is in the cart
                messages.info(request, "המוצר נוסף לעגלה")

        else:
            order = Order.objects.create(business_owner=products.shop_id, user=user)
            order.products.add(order_item)  # Adds a new product to the cart
            messages.info(request, "המוצר נוסף לעגלה")
    else:
        messages.info(request, "המוצר לא זמין במלאי")
    return redirect('/account/business_profile/{0}/'.format(products.shop_id_id))


def remove_from_cart(request, **kwargs):
    user = request.user
    products = get_object_or_404(product, id=kwargs.get('item_id', ""))  # Get a unique product ID in the store
    user_order = Order.objects.filter(user=user, business_owner=products.shop_id, customer_ready=False)
    if user_order.exists():
        order = user_order[0]
        # Remove
        if order.products.filter(product_id=products.id).exists():
            order_item = OrderItem.objects.filter(product_id=kwargs.get('item_id', ""), user=user, ordered=False)[0]
            if order_item.quantity > 1:  # If there is more than 1 quantity of the product then remove 1
                order_item.quantity -= 1
                order_item.save()
                messages.info(request, "המוצר הוסר מהעגלה")
            else:
                order.products.remove(order_item)  # If there is only product 1 then delete it completely from the cart
                messages.info(request, "המוצר הוסר מהעגלה")
        else:  # Message that a product that does not exist in the cart cannot be downloaded
            messages.info(request, "אין אפשרות להוריד מוצר שלא קיים בעגלה")
            return redirect('/account/business_profile/{0}/'.format(products.shop_id_id))
    else:
        messages.info(request, "אין הזמנה קיימת")
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
        o_t = True if request.POST.get('take_away') == "on" else False
        order = Order.objects.filter(user=user, business_owner=busi_id, customer_ready=False).update(
            customer_ready=True, order_comments=request.POST.get('comment'), order_type=o_t)

        # update the new amount of each product in the business
        for orde in existing_order.get_cart_items():
            element = product.objects.get(id=orde.product_id)
            OrderItem.objects.filter(user=user).update(ordered=True)
            prod = product.objects.filter(shop_id=busi_id, id=orde.product_id).update(
                product_amount=element.product_amount - orde.quantity)

        return redirect('/account/business_profile/{0}/'.format(busi_id))
    return render(request, 'cart.html', context)


def show_orders(request, busi_id):
    orders = Order.objects.filter(business_owner=busi_id)
    context = {'orders': orders, 'business': busi_id}
    if request.method == 'POST':
        user = request.user
        # get the order id by the id
        id = request.POST.get('order_id')
        req_order = Order.objects.get(id=id)  # update the status to ready
        req_order.status = True
        req_order.save()
        return redirect('/cart/show_orders/{0}/'.format(busi_id))
    return render(request, 'showOrders.html', context)


def history_orders(request, busi_id):
    orders = Order.objects.filter(business_owner=busi_id, status=True)
    context = {'orders': orders, 'business': busi_id}
    return render(request, 'history_orders.html', context)


def customer_orders(request):
    orders = Order.objects.filter(user=request.user)
    context = {'orders': orders}
    return render(request, 'customer_orders.html', context)


def business_report(request):
    return render(request, 'business_report.html')
