from .models import Task
from django.shortcuts import render

def mytodo(request):
    tasks = Task.objects.all()
    if request.method == 'POST':
        new_task = Task(title=request.POST['title'])
        new_task.save()
    return render(request,'home.html', {'tasks' : tasks})
