from django.urls import path

from . import views

urlpatterns = [

    # ----------Review interface----------------------------------
    path('<str:busi_id>/', views.commentt, name='comment'),

]
