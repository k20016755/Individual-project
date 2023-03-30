import pytest
from django.conf import settings

def pytest_configure():
    settings.DEBUG = False
    settings.DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:',
        }
    }
