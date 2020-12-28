from django.urls import path

from . import views

urlpatterns = [

    path('create_product', views.create_product, name = 'create_product'),
    path('update_product/<str:pk_test>/', views.update_product, name="update_product"),
    path('create_order/<str:pk>/', views.createOrder, name="create_order"),

]