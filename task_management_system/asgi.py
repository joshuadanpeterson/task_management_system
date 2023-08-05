"""
ASGI config for task_management_system project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# The line `os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_management_system.settings')` is setting the value of the environment variable `DJANGO_SETTINGS_MODULE` to 'task_management_system.settings'`.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_management_system.settings')

application = get_asgi_application()
