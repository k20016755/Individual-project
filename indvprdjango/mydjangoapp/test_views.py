
import os
import django

from mydjangoapp.models import Task

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'indvprdjango.settings')
django.setup()

@pytest.mark.django_db
def test_task_creation():
    task = Task.objects.create(title='Test task')
    assert task.title == 'Test task
