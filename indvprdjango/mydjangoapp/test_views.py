import django
import pytest
from django.urls import reverse
from mydjangoapp.models import Task
import django
from django.conf import settings
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","indvprdjango.settings")
django.setup()
@pytest.mark.django_db
def test_task_list(client):
    task1 = Task.objects.create(title='Task 1', completed=False)
    task2 = Task.objects.create(title='Task 2', completed=True)
    url = reverse('task_list')
    response = client.get(url)
    assert response.status_code == 200
    assert task1.title in str(response.content)
    assert task2.title in str(response.content)
    assert 'True' in str(response.content)