# WSGI (Web Server Gateway Interface) entry point for Django.
# This file allows the tokyoGas project to serve traditional synchronous HTTP requests.
# Used by WSGI servers (e.g., Gunicorn, uWSGI) for production deployments.
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
application = get_wsgi_application()
