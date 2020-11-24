from django.urls import path

from . import views

urlpatterns = [

    path('home', views.home, name = 'home'),
    path('abut', views.Abutus, name="AbutUs")
    
    # path('send', views.send, name = 'send')

]
