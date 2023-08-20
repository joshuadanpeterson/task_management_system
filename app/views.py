# This is the view for the login page. It will authenticate the user and log them in if the credentials are correct.
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from app.models import Task
from app.forms import CustomUserCreationForm, TaskForm

# This is the view for the login page. It will authenticate the user and log them in if the credentials are correct.
def user_login(request):
    """
    The function `user_login` handles user login requests, authenticates the user, and redirects to a
    success page if the login is successful, otherwise it renders the login page with an error message. 
     """
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is None:
            # Return an 'invalid login' error message.
            return render(request, 'login.html', {'error': 'Invalid login credentials'})
        login(request, user)
        return redirect('task_list')
    return render(request, 'login.html')

# This is the view for the logout page. It will log the user out and redirect them to the landing page.
def user_logout(request):
    logout(request)
    return redirect('landing_page')  # Replace 'landing_page' with the name of your homepage URL pattern

# New view for user signup
def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('task_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


# The function `landing_page` renders the landing page for the application.
def landing_page(request):
    return render(request, 'homepage/landing.html')

# The function 'task_list' renders the task list for the application.
@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

# The function `task_create` renders the task creation form and handles the creation of tasks.
@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    print(form.errors)
    return render(request, 'tasks/task_form.html', {'form': form})

# The function `task_detail` renders the task detail page for the application.
@login_required
def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    return render(request, 'tasks/task_detail.html', {'task': task})

# The function `task_edit` renders the task edit page for the application.
@login_required
def task_edit(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_detail', task_id=task_id)
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form, 'task': task})

# The function `task_delete` renders the task delete page for the application.
@login_required
def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})