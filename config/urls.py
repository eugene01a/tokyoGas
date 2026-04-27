from django.contrib import admin
from django.urls import path, include

# Root routing delegates app-level routes to the accounts app.
urlpatterns = [
    path('admin/', admin.site.urls),
    # Includes all URL patterns from the accounts app at the root path (''),
    # so /register/, /api/register/, etc. are handled by accounts.urls.
    path('', include('accounts.urls')),
]
