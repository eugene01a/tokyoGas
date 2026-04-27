#!/usr/bin/env python3
import os
import sys

# Entry point for Django CLI commands: manage.py runserver, migrate, test, etc.
def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            'Could not import Django. Are you sure it is installed and available on your PYTHONPATH?'
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
