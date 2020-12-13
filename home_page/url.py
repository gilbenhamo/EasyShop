from django.urls import path

from . import views

urlpatterns = [

    path('', views.home, name = 'home'),
    path('abut', views.Abutus, name="AbutUs"),
    path('Registar', views.Registar, name="Registar"),
    path('feedback', views.feedback, name="feedback"),
    # path('send', views.send, name = 'send')

]
