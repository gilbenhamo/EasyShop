from django.urls import path
from cart.views import customer_orders

from . import views

urlpatterns = [

    path('', views.home, name = 'home'),
    path('abut', views.Abutus, name="AbutUs"),
    path('Registar', views.Registar, name="Registar"),
    path('feedback', views.feedback, name="feedback"),
    path('searchByCategory/<str:categ>/', views.searchByCategory, name="searchByCategory"),
    path('search/', views.search, name="search"),
    path('admin_reports', views.adminReports, name="admin_reports"),
    path('customer_orders/', customer_orders, name='customer_orders'),
    # path('send', views.send, name = 'send')

]
