from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .models import Login, Register
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import redirect
from django.contrib.auth import logout

def index(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = Login.objects.get(email=email)
            if check_password(password, user.password):
                request.session['user_id'] = user.id
                messages.success(request, 'Login successful')
                return redirect('home')
            else:
                messages.error(request, 'Invalid email or password')
        except Login.DoesNotExist:
            messages.error(request, 'Invalid email or password')

    return render(request, 'login.html')

def register_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        parent_name = request.POST['parent_name']
        mobile = request.POST['mobile']
        role = request.POST['role']
        address = request.POST['address']

        hashed_password = make_password(password)
        login_entry = Login.objects.create(email=email, password=hashed_password)
        register_entry = Register.objects.create(
            login=login_entry,
            parent_name=parent_name,
            mobile=mobile,
            role=role,
            address=address
        )

        messages.success(request, 'Registration successful. Please login.')
        return redirect('login')

    return render(request, 'register.html')

def home(request):
    if 'user_id' in request.session:
        return render(request, 'home.html')
    else:
        return redirect('login')
    
def logout_view(request):
    logout(request)
    return redirect('index')



def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = Login.objects.get(email=email)
            if check_password(password, user.password):
                request.session['user_id'] = user.id
                messages.success(request, 'Login successful')
                return redirect('home')
            else:
                messages.error(request, 'Invalid email or password')
        except Login.DoesNotExist:
            messages.error(request, 'Invalid email or password')

    return render(request, 'login.html')
