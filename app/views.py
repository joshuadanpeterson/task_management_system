# This is the view for the login page. It will authenticate the user and log them in if the credentials are correct.
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


def user_login(request):
    """
    The function `user_login` handles user login requests, authenticates the user, and redirects to a
    success page if the login is successful, otherwise it renders the login page with an error message.
    
    :param request: The `request` parameter is an object that represents the HTTP request made by the
    user. It contains information about the request, such as the method used (e.g., GET or POST), the
    URL being accessed, any data sent with the request, and more
    :return: a rendered HTML template called 'login.html' if the request method is not "POST". If the
    request method is "POST", it will either redirect to a success URL or render the 'login.html'
    template with an error message if the login credentials are invalid.
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
