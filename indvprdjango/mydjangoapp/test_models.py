import pytest
from mydjangoapp.models import Task

@pytest.mark.django_db
def test_create_task():
    task = Task.objects.create(title='Task 1', completed=False)
    assert task.title == 'Task 1'
    assert task.completed == False

@pytest.mark.django_db
def test_update_task():
    task = Task.objects.create(title='Task 2', completed=False)
    task.completed = True
    task.save()
    assert task.completed == True

@pytest.mark.django_db
def test_delete_task():
    task = Task.objects.create(title='Task 3', completed=False)
    task.delete()
    assert Task.objects.filter(title='Task 3').exists() == False