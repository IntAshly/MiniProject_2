from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from .models import User
from django.contrib import messages

def register_view(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']

        if User.objects.filter(username=email).exists():
            messages.error(request, 'An account with this email already exists.')
            return redirect('register')

        # Create a user
        user = User.objects.create_user(
            username=email, 
            first_name=first_name, 
            last_name=last_name, 
            email=email, 
            phone=phone, 
            password=password
        )
        user.save()

        # Authenticate and log in the user
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Account created for {email}!')
            return redirect('role')  # Redirect to the role selection page
        
    return render(request, 'register.html')

def role_view(request):
    if request.method == 'POST':
        role = request.POST['role']
        if request.user.is_authenticated:
            user = User.objects.get(id=request.user.id)  # Fetch the logged-in user
            user.usertype = '0' if role == 'parent' else '1'
            user.save()
            
            if role == 'parent':
                return redirect('login')  # Redirect to login page for parents
            elif role == 'healthcare_provider':
                return redirect('health_profile')  # Redirect to health profile for healthcare providers
        else:
            messages.error(request, 'User is not authenticated.')
            return redirect('login')  # Redirect to login page
    
    return render(request, 'role.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        
        # Check for admin credentials first
        if username == 'admin@gmail.com' and password == 'admin':
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('admin')  # Redirect to admin page

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.usertype == '0':  # Parent
                return redirect('home')  # Redirect to home page for parents
            elif user.usertype == '1':  # Healthcare provider
                return redirect('health_profile')  # Redirect to healthcare provider home page
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

def user_index(request):
    return render(request, 'user/userindex.html')

def logout_view(request):
    logout(request)
    return redirect('index')

def health_profile_view(request):
    return render(request, 'health_profile.html')

def index_view(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def admin_view(request):
    return render(request, 'admin.html')
