# models.py
from django.db import models

# Model for storing login credentials
class Login(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Store hashed passwords securely

# Model for storing user registration details
class Register(models.Model):
    login = models.OneToOneField(Login, on_delete=models.CASCADE)
    parent_name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    role = models.CharField(max_length=20, choices=[('parent', 'Parent'), ('healthcare_provider', 'Healthcare Provider')])
    address = models.TextField()
