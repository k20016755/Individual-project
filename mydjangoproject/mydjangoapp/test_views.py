import pytest
from django.urls import reverse
from django.test import TestCase,RequestFactory
from mydjangoapp.views import task_list
class TESTVIEWS(TestCase):
    @pytest.mark.django_db
    def test_task_list_view(self):
        factory = RequestFactory()
        request = factory.get(reverse('task_list'))
        response = task_list(request)
        self.assertContains(response,'<h1>Task List<h1>')
        self.assertTemplateUsed('mydjangoapp/templates/task_list.html')
        assert response.status_code == 200
    


