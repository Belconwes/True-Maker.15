from django.contrib.auth import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from .models import User
from django.forms import ModelForm


class Userform(UserCreationForm):
    
    class Meta:
        model = User
        
        fields = ('email','nombre','apellido','password1','password2')
        
        
class Authformi(AuthenticationForm):
    
    
    class Meta:
         model = User
        
         fields = ('email','password')

        