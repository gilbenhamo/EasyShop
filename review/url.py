from django.urls import path

from review import views

urlpatterns = [

    # path('login_r', views.login_r, name="login_r"),
    # path('logout', views.logout, name="logout"),
    # path('customer_register/', views.customer_register.as_view(), name='customer_register'),
    # path('business_register/', views.business_register.as_view(), name='business_register'),
    path('<str:busi_id>/', views.commentt, name='comment'),
    # path('update_business/<str:pk_test>/', views.update_business, name="update_business"),
    # path('create_Massage/<str:pk_test>/', views.create_Massage, name="create_Massage"),
    # path('create_deals/<str:pk_test>/', views.create_deals, name="create_deals"),
    # path('update_Category/', views.update_Category, name='update_Category'),

    # path('send', views.send, name = 'send')

]
