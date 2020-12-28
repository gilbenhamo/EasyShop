from django.urls import path

from . import views

urlpatterns = [

    path('<str:busi_id>/', views.show_cart, name='commentt'),

]
