from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    location = forms.CharField(required=False, max_length=255, label="Location")

    class Meta:
        model = CustomUser
        fields = ("username", "email", "password1", "password2", "location")

class CustomLoginForm(AuthenticationForm):
    remember_me = forms.BooleanField(required=False, label="Remember Me")
