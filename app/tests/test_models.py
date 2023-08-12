# Inside tests/test_models.py
import pytest
from django.contrib.auth.models import User
from app.models import UserProfile, Task

@pytest.mark.django_db
def test_user_profile_creation():
    user = User.objects.create_user(username='testuser', password='12345')
    profile = UserProfile.objects.create(user=user)
    assert profile.user == user

@pytest.mark.django_db
def test_task_creation():
    user = User.objects.create_user(username='testuser2', password='12345')
    task = Task.objects.create(user=user, title="Test Task", description="Test Description", due_date="2023-08-04", due_time="13:00:00")
    assert task.status == Task.STATUS_PENDING

@pytest.mark.django_db
def test_task_status_update():
    user = User.objects.create_user(username='testuser3', password='12345')
    task = Task.objects.create(user=user, title="Test Task 2", description="Test Description 2", due_date="2023-08-05", due_time="14:00:00")
    task.status = Task.STATUS_COMPLETED
    task.save()
    updated_task = Task.objects.get(id=task.id)
    assert updated_task.status == Task.STATUS_COMPLETED
