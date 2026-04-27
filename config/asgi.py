# ASGI (Asynchronous Server Gateway Interface) entry point for Django.
# This file allows the tokyoGas project to serve asynchronous protocols (like WebSockets) and async HTTP requests.
# Used by ASGI servers (e.g., Daphne, Uvicorn) for modern, async-capable deployments.
import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
application = get_asgi_application()
