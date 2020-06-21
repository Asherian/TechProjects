from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from . import views


def admin_console(request):
    products = Product.objects.all()
    return render(request, 'products/product_page.html', {'products': products}),

