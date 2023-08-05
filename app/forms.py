# The code is importing necessary modules and classes from the Django framework for creating user registration forms.
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# This class is used to create a user registration form.
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

