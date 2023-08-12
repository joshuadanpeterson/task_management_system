# Testing the 'user_login' view in views.py
from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User

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
        self.assertContains(response, 'Invalid login credentials')

# Testing the 'task_create' view in views.py
from app.models import Task

class TaskCreateViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.task_create_url = reverse('task_create')  # Assuming the name of the task create URL pattern is 'task_create'

    def test_task_creation_with_valid_data(self):
        data = {
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

# Test the 'task_delete' view in views.py
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
