from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class user_create(User):
    fields = ['username','password','is_active','date_joined','email']
    
