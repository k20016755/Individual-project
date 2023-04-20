import pytest
from django.urls import reverse
from django.test import TestCase,Client
from mydjangoapp.views import task_list
from django.contrib.auth.models import User
import datetime
from datetime import date
from django.utils import timezone
from mydjangoapp.models import Task
import random
from django.db.utils import IntegrityError
class TESTVIEWS(TestCase):
    def setUp(self):
        self.client = Client()
        #try:
         #   self.user = User.objects.get(username='testuser')
        #except User.DoesNotExist:
         #   self.user = User.objects.create_user(username='testuser', password='testpass')
        self.user = User.objects.create_user(username='16177', password='Alpha123')
        self.task1 = Task.objects.create(
            
            title="Task 1",
            description="Description 1",
            completed=False,
            created_at=timezone.now(),
            updated_at=timezone.now(),
            
        )
        self.client = Client()
        #try:
         #   self.user = User.objects.get(username='testuser')
        #except User.DoesNotExist:
        self.user = User.objects.create_user(username='20016755', password='Tiger679')
         #   self.user = User.objects.create_user(username='testuser', password='testpass')
        self.task2 = Task.objects.create(
            

            title="Task 2",
            description="Description 2",
            completed=True,
            created_at=timezone.now(),
            updated_at=timezone.now(),
            
        )
    
    def test_task_list_view(self):     
        #try:
        user = User.objects.create_user(username='16177',password='Alpha123')
        #except IntegrityError:
        # The username already exists, so generate a new unique username
        # You can use any method to generate a unique username
         #   username = 'testuser' + str(random.randint(1000, 9999))
          #  user = User.objects.create_user(username=username, password='testpass')
        self.client.login(user)
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.task1.title)
        self.assertContains(response, self.task2.title)
    

       
        assert response.status_code == 200
    


