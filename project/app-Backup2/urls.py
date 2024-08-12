from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('role/', views.role_view, name='role'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('health_profile/', views.health_profile_view, name='health_profile'),
     path('admin/', views.admin_view, name='admin'),
]
