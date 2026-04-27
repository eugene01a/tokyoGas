import re
from django.core.exceptions import ValidationError
from django.core.validators import validate_email as django_validate_email
from django.contrib.auth import get_user_model
from .models import Pref

# Shared validation helpers used by both forms and serializers.

def validate_username(username):
    if not username or len(username.strip()) < 3:
        raise ValidationError('Username must be at least 3 characters long.')
    return username


# Validate email syntax and enforce uniqueness for registration.
def validate_email(email):
    try:
        django_validate_email(email)
    except ValidationError:
        raise ValidationError('Enter a valid email address.')

    User = get_user_model()
    if User.objects.filter(email__iexact=email).exists():
        raise ValidationError('A user with this email already exists.')
    return email


# Enforce the password policy required by the registration flow.
def validate_password(password):
    if len(password or '') < 8:
        raise ValidationError('Password must be at least 8 characters long.')
    if not re.search(r'[A-Z]', password):
        raise ValidationError('Password must contain at least one uppercase letter.')
    if not re.search(r'[a-z]', password):
        raise ValidationError('Password must contain at least one lowercase letter.')
    if not re.search(r'[0-9]', password):
        raise ValidationError('Password must contain at least one digit.')
    return password


# Simple digit-only validation for telephone numbers.
def validate_tel(tel):
    if tel and not tel.isdigit():
        raise ValidationError('Telephone number must contain digits only.')
    return tel

# Ensure pref ID maps to a valid Pref record.
def validate_pref(pref_id):
    if not pref_id:
        raise ValidationError('Please select a prefecture.')
    if isinstance(pref_id, Pref):
        return pref_id
    if not Pref.objects.filter(pk=pref_id).exists():
        raise ValidationError('Selected prefecture does not exist.')
    return Pref.objects.get(pk=pref_id)
