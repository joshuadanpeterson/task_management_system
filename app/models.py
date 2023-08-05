# This file defines the models for the app. The models are used to create the database tables.
from django.db import models
from django.contrib.auth.models import User  # Import the built-in User model

# The below class defines a UserProfile model with a one-to-one relationship with the built-in User model.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

# The below class defines a Task model with various fields such as user, title, description, due date,
# due time, and status.
class Task(models.Model):
    # Status of the task
    STATUS_PENDING = 'Pending'
    STATUS_IN_PROGRESS = 'In Progress'
    STATUS_COMPLETED = 'Completed'
    STATUS_ON_HOLD = 'On Hold'
    STATUS_CANCELLED = 'Cancelled'
    
    STATUS_CHOICES = [
        (STATUS_PENDING, 'Pending'),
        (STATUS_IN_PROGRESS, 'In Progress'),
        (STATUS_COMPLETED, 'Completed'),
        (STATUS_ON_HOLD, 'On Hold'),
        (STATUS_CANCELLED, 'Cancelled'),
    ]
    
    # task_id will be automatically created as an ID field by Django.
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # References user_id in the built-in User model
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    due_time = models.TimeField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=STATUS_PENDING)
