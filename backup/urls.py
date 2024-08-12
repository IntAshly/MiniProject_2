# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_user, name='register'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout_view, name='logout'),
]
