from django.urls import path
from cart.views import add_to_cart, remove_from_cart,business_report
from . import views

urlpatterns = [
    # ----------Registration and login system interface----------------------------------
    path('login_r', views.login_r, name="login_r"),
    path('logout', views.logout, name="logout"),
    path('customer_register/', views.customer_register.as_view(), name='customer_register'),
    path('business_register/', views.business_register.as_view(), name='business_register'),

    # ----------Business profile system profile interface----------------------------------
    path('business_profile/<str:pk_test>/', views.business_profile, name='business_profile'),
    path('update_business/<str:pk_test>/', views.update_business, name="update_business"),
    path('create_Massage/<str:pk_test>/', views.create_Massage, name="create_Massage"),
    path('create_deals/<str:pk_test>/', views.create_deals, name="create_deals"),
    path('business_report/', business_report, name="business_report"),
    path('sales_report/', views.sales_report, name="sales_report"),
    path('money_report/', views.money_report, name="money_report"),
    path('Inventory_report/', views.Inventory_report, name="Inventory_report"),

    # ----------Customer profile system profile interface----------------------------------
    path('add-to-cart/<str:item_id>/', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<str:item_id>/', remove_from_cart, name='remove_from_cart'),

    # ----------admin interface----------------------------------
    path('update_Category/', views.update_Category, name='update_Category'),

]

