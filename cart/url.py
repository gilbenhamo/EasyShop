from django.urls import path

from . import views

urlpatterns = [

    path('<str:busi_id>/', views.show_cart, name='show_cart'),
    path('show_orders/<str:busi_id>/', views.show_orders, name='show_orders'),
    path('history_orders/<str:busi_id>/', views.history_orders, name='history_orders'),
    # path('ready_customer_orders/<str:busi_id>', views.ready_customer_orders, name='ready_customer_orders'),

]
