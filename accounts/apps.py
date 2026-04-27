from django.apps import AppConfig


class AccountsConfig(AppConfig):
    # Configuration class for the 'accounts' Django app.
    # Sets the default auto field type for models and specifies the app name.
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
