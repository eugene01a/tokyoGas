from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from .models import Pref

def registration_complete_view(request):
    # View for the registration completion page, shown after successful user registration.
    return render(request, 'accounts/registration_complete.html')


def register_view(request):
    # Serve the React-based registration page.
    return render(request, 'accounts/react_registration.html', {'api_base_url': '/api'})
