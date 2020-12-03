from django.urls import path

from . import views

urlpatterns = [

    path('login_r', views.login_r, name="login_r"),
    path('logout', views.logout, name="logout"),
    path('customer_register/', views.customer_register.as_view(), name='customer_register'),
    path('business_register/', views.business_register.as_view(), name='business_register')

    # path('send', views.send, name = 'send')

]
