from django.urls import path
from . import views
from .api_views import PrefListAPIView, UserRegistrationAPIView

app_name = 'accounts'

urlpatterns = [
    # Web form routes
    path('register/', views.register_view, name='register'),
    path('register/complete/', views.registration_complete_view, name='registration_complete'),
    path('register/react/', views.react_registration_view, name='react_registration'),

    # API endpoints for frontend integration.
    path('api/register/', UserRegistrationAPIView.as_view(), name='api_register'),
    path('api/prefs/', PrefListAPIView.as_view(), name='api_prefs'),
]
