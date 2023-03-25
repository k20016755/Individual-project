from operator import mod
from django.db import models
class Task(models.Model):
    class Meta():
        app_label='mydjangoapp'
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
