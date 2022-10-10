from django.contrib import admin
from django.urls import path
from nftapp import views

urlpatterns = [
    path('index/', views.index,name='index'),
    path('addaddress/', views.address_to_allowlist, name='index'),
    path('contract/', views.deploy_contract, name='index'),
    # path('image/', views.mint_image, name='index'),
    path('con/', views.custom_contract, name='index'),
]

