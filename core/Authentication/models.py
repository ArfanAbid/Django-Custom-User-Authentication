from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager

# Create your models here.

class CustomUser(AbstractUser):
    username=None
    email=models.EmailField(unique=True)
    phone_number=models.CharField(max_length=100,blank=True) #unique=True
    address=models.CharField(max_length=200)
    
    

    USERNAME_FIELD="email"   # identifier for the user model instead of the default   `username` field. This means that when  authenticating a user, the `email` field will be used instead of the `username` field.

    REQUIRED_FIELDS=[]   # The `REQUIRED_FIELDS` attribute is used in Django's authentication system to specify which fields are required when creating a user. By default, Django's `AbstractUser` model requires a username and password. However, in this case, the `CustomUser` model is using the email field as the identifier instead of the username field.
    
    
    
    
    objects = UserManager()