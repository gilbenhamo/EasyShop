from django.urls import path

from . import views

urlpatterns = [

    path('custmer', views.custmer, name="custmer"),

    # path('send', views.send, name = 'send')

]
