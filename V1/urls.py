from django.urls import path

from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path('stores/', views.stores, name='stores'),
    path('keywords/', views.keywords, name="keywords"),
    path('demo/', views.demoProducts, name ="demo"),
    path('cart/', views.cartInfo, name="cartInfo")
]
