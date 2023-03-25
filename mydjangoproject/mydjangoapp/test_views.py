import pytest
from django.urls import reverse
from django.test import RequestFactory
from mydjangoapp.views import task_list

@pytest.mark.django_db
def test_task_list_view():
    factory = RequestFactory()
    request = factory.get(reverse('task_list'))
    response = task_list(request)
    assert response.status_code == 200
