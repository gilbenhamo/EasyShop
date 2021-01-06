from django.urls import path
from cart.views import customer_orders

from . import views

urlpatterns = [

    # ----------General interface for displaying pages on the site----------------------------------
    path('', views.home, name = 'home'),
    path('abut', views.Abutus, name="AbutUs"),
    path('Registar', views.Registar, name="Registar"),
    path('feedback', views.feedback, name="feedback"),
    path('searchByCategory/<str:categ>/', views.searchByCategory, name="searchByCategory"),
    path('search/', views.search, name="search"),
    path('guides/', views.guides, name='guides'),

    # ----------A cart-related consumer interface--------------------------------------------------
    path('admin_reports', views.adminReports, name="admin_reports"),

    # ----------Admin interface-------------------------------------------------------------------
    path('customer_orders/', customer_orders, name='customer_orders'),

]
