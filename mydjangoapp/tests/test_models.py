import pytest
from mydjangoapp.models import Task
import mydjangoproject

@pytest.mark.django_db
def test_create_task():
    task = Task.objects.create(title='Test Task', description='Test description')
    assert task.description == 'Test description'
    assert task.title == 'Test Task'
    
