# The code is importing necessary modules and classes from the Django framework for creating user registration forms.
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Task

# This class is used to create a user registration form.
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

# This class is used to represent the Task model in form format.
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['user', 'title', 'description', 'due_date', 'due_time', 'status']
