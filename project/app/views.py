from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from .models import User
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def index_view(request):
    return render(request, 'index.html')

def register_view(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        
        user = User.objects.create_user(username=email, first_name=first_name, last_name=last_name, email=email, phone=phone, password=password)
        user.save()
        
        messages.success(request, f'Account created for {email}!')
        return redirect('login')
        
    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:	
            login(request, user)
            return redirect('home')  # Replace 'dashboard' with your desired redirect URL after login
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

def user_index(request):
    return render(request, 'user/userindex.html')

def logout_view(request):
    logout(request)
    return redirect('index')
