# This is the view for the login page. It will authenticate the user and log them in if the credentials are correct.
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from app.models import Task
from app.forms import TaskForm

def user_login(request):
    """
    The function `user_login` handles user login requests, authenticates the user, and redirects to a
    success page if the login is successful, otherwise it renders the login page with an error message. 
     """
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('some_success_url')
        else:
            # Return an 'invalid login' error message.
            return render(request, 'login.html', {'error': 'Invalid login credentials'})
    return render(request, 'login.html')
