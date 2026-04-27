from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from .models import Pref


def register_view(request):
    # Server-rendered registration form with backend validation.
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:registration_complete')
    else:
        form = UserRegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})


def registration_complete_view(request):
    # View for the registration completion page, shown after successful user registration.
    return render(request, 'accounts/registration_complete.html')


def react_registration_view(request):
    # Serve the React-based registration page.
    return render(request, 'accounts/react_registration.html', {'api_base_url': '/api'})
