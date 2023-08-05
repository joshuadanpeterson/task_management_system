from django.contrib import admin
from django.urls import path, # re_path, include
from app import views  # Assuming your app's name is 'app'
from django.contrib.auth import views as auth_views  # Import built-in authentication views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # User registration or signup view
    path('signup/', views.signup_view, name='signup'),
    
    # User login view
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    
    # User logout view
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # CRUD operations on tasks
    # e.g., 
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/create/', views.task_create, name='task_create'),
    path('tasks/<int:task_id>/', views.task_detail, name='task_detail'),
    path('tasks/<int:task_id>/edit/', views.task_edit, name='task_edit'),
    path('tasks/<int:task_id>/delete/', views.task_delete, name='task_delete')

    # re_path(r'^$', include('app.urls')),  # This will include all URLs from the 'app' at the root
]
