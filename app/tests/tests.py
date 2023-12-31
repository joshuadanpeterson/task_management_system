# Inside app/tests/tests.py

import pytest
from django.contrib.auth.models import User
from app.models import UserProfile, Task
from django.urls import reverse
from django.test import TestCase

# Model Tests
class TestModels(TestCase):

    def test_user_profile_creation(self):
        user = User.objects.create_user(username='testuser', password='12345')
        profile = UserProfile.objects.create(user=user)
        self.assertEqual(profile.user, user)

    def test_task_creation(self):
        user = User.objects.create_user(username='testuser2', password='12345')
        task = Task.objects.create(user=user, title="Test Task", description="Test Description", due_date="2023-08-04", due_time="13:00:00")
        self.assertEqual(task.status, Task.STATUS_PENDING)

    def test_task_status_update(self):
        user = User.objects.create_user(username='testuser3', password='12345')
        task = Task.objects.create(user=user, title="Test Task 2", description="Test Description 2", due_date="2023-08-05", due_time="14:00:00")
        task.status = Task.STATUS_COMPLETED
        task.save()
        updated_task = Task.objects.get(id=task.id)
        self.assertEqual(updated_task.status, Task.STATUS_COMPLETED)



# View Tests
class UserLoginViewTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.login_url = reverse('login')  # Assuming the name of the login URL pattern is 'user_login'

    def test_successful_login(self):
        response = self.client.post(self.login_url, {'username': 'testuser', 'password': '12345'})
        self.assertEqual(response.status_code, 302)  # Expecting a redirect
        self.assertRedirects(response, reverse('task_list'))  # Replace 'some_success_url' with the name of your success URL pattern

    def test_unsuccessful_login(self):
        response = self.client.post(self.login_url, {'username': 'testuser', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 200)  # Expecting to stay on the same page
        self.assertContains(response, 'error')
        print(response.content.decode())


# Tests for task creation
class TaskCreateViewTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.task_create_url = reverse('task_create')  # Assuming the name of the task create URL pattern is 'task_create'

    def test_task_creation_with_valid_data(self):
        data = {
            'user': self.user.id,
            'title': 'Test Task',
            'description': 'This is a test task description',
            'due_date': '2023-12-31',
            'due_time': '12:00',
            'status': Task.STATUS_PENDING
        }
        response = self.client.post(self.task_create_url, data)
        self.assertEqual(response.status_code, 302)  # Expecting a redirect
        self.assertRedirects(response, reverse('task_list'))  # Assuming the name of the task list URL pattern is 'task_list'
        self.assertEqual(Task.objects.count(), 1)  # One task should be created

    def test_task_creation_with_invalid_data(self):
        data = {
            'title': '',  # Empty title
            'description': 'This is a test task description',
            'due_date': '2023-12-31',
            'due_time': '12:00',
            'status': Task.STATUS_PENDING
        }
        response = self.client.post(self.task_create_url, data)
        self.assertEqual(response.status_code, 200)  # Expecting to stay on the same page
        self.assertEqual(Task.objects.count(), 0)  # No task should be created


# Tests for task deletion
class TaskDeleteViewTests(TestCase):
   
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

        # Create a task
        self.task = Task.objects.create(
            user=self.user,
            title='Test Task',
            description='This is a test task description',
            due_date='2023-12-31',
            due_time='12:00',
            status=Task.STATUS_PENDING
        )
        self.task_delete_url = reverse('task_delete', args=[self.task.id])  # Assuming the name of the task delete URL pattern is 'task_delete'

    def test_task_deletion(self):
        # At the start, there should be one task
        self.assertEqual(Task.objects.count(), 1)
        
        response = self.client.post(self.task_delete_url)
        
        # After deletion, there should be no tasks left
        self.assertEqual(Task.objects.count(), 0)
        self.assertEqual(response.status_code, 302)  # Expecting a redirect after deletion
        self.assertRedirects(response, reverse('task_list'))  # Assuming the name of the task list URL pattern is 'task_list'