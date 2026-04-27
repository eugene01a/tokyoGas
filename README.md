# Tokyo Gas Registration Project

This repository contains a Django demonstration project for Tokyo Gas registration requirements.

## Structure
- `config/` - Django project settings and configuration
- `accounts/` - Django app containing the custom user model, registration form, API, and tests
- `templates/accounts/` - server-rendered templates for registration and completion pages
- `frontend/` - React frontend app sources for realtime validation and API integration
- `static/` - Django static files directory (contains built React assets)
- `requirements.txt` - Python dependencies

## Features
- Custom user model inheriting from `AbstractUser`
- `tel` and `pref` fields added to user
- Server-side validation for username, email, password, telephone, and prefecture
- REST API registration endpoint using Django REST Framework
- React frontend for realtime client-side validation and API submission
- Database fixtures for all 47 Japanese prefectures
- Email uniqueness enforced at database level

## Setup
1. Install Python dependencies
   ```bash
   pip install -r requirements.txt
   ```
2. Apply migrations and load fixtures
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py loaddata accounts/fixtures/prefectures.json
   ```
3. Create a superuser (optional, for admin access)
   ```bash
   python manage.py createsuperuser
   ```
4. Run the development server
   ```bash
   python manage.py runserver
   ```

## URLs
- `/register/` - Django form-based registration
- `/register/react/` - React frontend registration
- `/api/register/` - REST API registration endpoint
- `/api/prefs/` - REST API prefecture list endpoint
- `/admin/` - Django admin interface

## Testing
- Backend tests: `python manage.py test accounts`
- Frontend tests: `cd frontend && npm test`

## Notes
- Python 3.10+ is recommended but 3.9.6 works for this demo
- React app is built and served as Django static files
- All prefecture data is pre-loaded via fixtures
- Email uniqueness is enforced at both application and database levels