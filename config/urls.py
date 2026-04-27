from django.contrib import admin
from django.urls import path, include

# Root routing delegates app-level routes to the accounts app.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
]
