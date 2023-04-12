import pytest
from django.conf import settings
#configuring django databases for pytest testing
def pytest_configure():
    settings.DEBUG = False
    settings.DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:',
        }
    }
