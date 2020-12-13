from django.urls import path

from . import views

urlpatterns = [

    path('login_r', views.login_r, name="login_r"),
    path('logout', views.logout, name="logout"),
    path('customer_register/', views.customer_register.as_view(), name='customer_register'),
    path('business_register/', views.business_register.as_view(), name='business_register'),
    path('business_profile/<str:pk_test>/', views.business_profile, name='business_profile'),
    path('update_business/<str:pk_test>/', views.update_business, name="update_business"),

    # path('send', views.send, name = 'send')

]
