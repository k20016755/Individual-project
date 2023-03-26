import pytest
from mydjangoapp.models import Task
import mydjangoproject
#import django
#django.setup()
from django.conf import settings
from pathlib import Path

from mydjangoproject.mydjangoproject.settings import BASE_DIR, DEBUG
settings.configure(
    DJANGO_SETTINGS_MODULE=mydjangoproject.settings,
    DEBUG=False,
    BASE_DIR = Path(__file__).resolve().parent.parent,
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    
}


)
@pytest.mark.django_db
def test_create_task():
    task = Task.objects.create(title='Test Task', description='Test description')
    assert task.title == 'Test Task'
    assert task.description == 'Test description'
