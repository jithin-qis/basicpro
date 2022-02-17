from itertools import product
from re import I
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import *
from django.contrib.auth.models import User


def user_login(request):
    form = AuthenticationForm(request.POST)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('get_products')
        return HttpResponse('User not found : %s'%username)
    return render(request, 'myapp/form_template.html', {'form':form})


def user_create(request):
    form = UserCreationForm(request.POST or None)
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password1')
            user = User.objects.create_user(username=username,password= password)
            user.save()
            return redirect('login')
        except:pass
    return render(request, 'myapp/form_template.html', {'form':form})


def product_create(request):
    form = ProductForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save()
            instance.owner = request.user
            instance.save()
            return redirect('get_products')
    return render(request, 'myapp/form_template.html', {'form':form})


def product_update(request, id):
    product = Product.objects.get(id=id)
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save()
            instance.owner = request.user
            instance.save()
            return redirect('get_products')
    return render(request, 'myapp/form_template.html', {'form':form})

def get_products(request):
    products = Product.objects.all()
    return render(request, 'myapp/products.html', {'products':products})

def delete_product(request, id):
    Product.objects.get(id=id).delete()
    return redirect('get_products')