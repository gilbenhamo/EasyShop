from django.urls import path

from . import views

urlpatterns = [

    # ----------Consumer ordering interface----------------------------------
    path('<str:busi_id>/', views.show_cart, name='show_cart'),

    # ----------Business ordering interface----------------------------------
    path('show_orders/<str:busi_id>/', views.show_orders, name='show_orders'),
    path('history_orders/<str:busi_id>/', views.history_orders, name='history_orders'),

]
