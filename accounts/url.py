from django.urls import path

from . import views

urlpatterns = [

    path('custmer', views.custmer, name="custmer"),
    path('Business', views.Business, name="Business"),

    # path('send', views.send, name = 'send')

]
