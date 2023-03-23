from asyncio import tasks
from django.shortcuts import render
from mydjangoapp.models import Task

def task_list(request):
    task = Task.objects.all()
    return render(request,'mydjangoapp/task_list.html',{'tasks':tasks})