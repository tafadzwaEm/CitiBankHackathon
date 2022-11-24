from django.urls import path
from .views import HomeView, ScanCodeView, ShowCodeView, Cart

urlpatterns = [
    path('',HomeView,name='home'),
    path('scan/',ScanCodeView,name='scan'),
    path('show/',ShowCodeView,name='show'),
    path('cart/',Cart.as_view(),name='cart'),
]