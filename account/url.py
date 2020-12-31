from django.urls import path
from cart.views import add_to_cart, remove_from_cart
from . import views

urlpatterns = [

    path('login_r', views.login_r, name="login_r"),
    path('logout', views.logout, name="logout"),
    path('customer_register/', views.customer_register.as_view(), name='customer_register'),
    path('business_register/', views.business_register.as_view(), name='business_register'),
    path('business_profile/<str:pk_test>/', views.business_profile, name='business_profile'),
    path('update_business/<str:pk_test>/', views.update_business, name="update_business"),
    path('create_Massage/<str:pk_test>/', views.create_Massage, name="create_Massage"),
    path('create_deals/<str:pk_test>/', views.create_deals, name="create_deals"),
    path('update_Category/', views.update_Category, name='update_Category'),
    path('add-to-cart/<str:item_id>/', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<str:item_id>/', remove_from_cart, name='remove_from_cart'),

    # path('send', views.send, name = 'send')

]

