from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    phone = models.CharField(max_length=15, null=True, blank=True)
    
    # Define choices for user types
    USER_TYPE_CHOICES = [
        ('admin', 'Admin'),
        ('parent', 'Parent'),
        ('healthcare_provider', 'Healthcare Provider'),
    ]
    
    usertype = models.CharField(
        max_length=20,
        choices=USER_TYPE_CHOICES,
    )
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # Add a related_name to avoid clash
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='Groups',
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',  # Add a related_name to avoid clash
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='User Permissions',
    )
    