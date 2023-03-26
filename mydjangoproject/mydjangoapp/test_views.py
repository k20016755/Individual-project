import pytest
from django.urls import reverse
from django.test import TestCase,RequestFactory
from mydjangoapp.views import task_list
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
class TESTVIEWS(TestCase):
    @pytest.mark.django_db
    def test_task_list_view(self):
        factory = RequestFactory()
        request = factory.get(reverse('task_list'))
        response = task_list(request)
        self.assertContains(response,'<h1>Task List<h1>')
        self.assertTemplateUsed('mydjangoapp/templates/task_list.html')
        assert response.status_code == 200
    


