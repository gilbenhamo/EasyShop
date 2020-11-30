from django.urls import path

from . import views

urlpatterns = [

    path('custmer', views.custmer, name="custmer"),
    path('Business', views.Business, name="Business"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),

    # path('send', views.send, name = 'send')

]
