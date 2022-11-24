from django.shortcuts import render
from django.views.generic import ListView
from .models import Product

def HomeView(request):
    return render(request,'payments/home.html')

def ScanCodeView(request):
    return render(request,'payments/scancode.html')

def ShowCodeView(request):
    return render(request,'payments/showcode.html')

class Cart(ListView):
    model = Product
    template_name = "payments/cart.html"
    context_object_name = "products"
