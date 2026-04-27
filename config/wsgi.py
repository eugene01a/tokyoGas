import os
from django.core.wsgi import get_wsgi_application

# WSGI entry point for traditional deployment servers.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
application = get_wsgi_application()
