#!/usr/bin/env python
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'learn_models.settings'
import sys


if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hello_django.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
    path = r'C:\Users\mc\PycharmProjects\hello_django\excelfile'
    #file_name(path)
