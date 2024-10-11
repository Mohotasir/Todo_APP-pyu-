from .models import Task
from django.shortcuts import get_object_or_404, redirect, render

def mytodo(request):
    # Fetch tasks based on completion status
    remaining_tasks = Task.objects.filter(isCompleted=False)
    completed_tasks = Task.objects.filter(isCompleted=True)

    if request.method == 'POST':
        # Add new task
        if 'title' in request.POST:
            new_task = Task(title=request.POST['title'])
            new_task.save()
            return redirect('mytodo')

        # Delete task
        elif 'delete_task' in request.POST:
            task_id = request.POST.get('task_id')
            task = get_object_or_404(Task, id=task_id)
            task.delete()
            return redirect('mytodo')

        # Toggle task completion
        elif 'done' in request.POST:
            task_id = request.POST.get('task_id')
            task = get_object_or_404(Task, id=task_id)
            task.isCompleted = not task.isCompleted  # Toggle the isCompleted status
            task.save()
            return redirect('mytodo')

    return render(request, 'home.html', {
        'remaining_tasks': remaining_tasks,
        'completed_tasks': completed_tasks
    })
def update_task(request, id):
    task = get_object_or_404(Task, id=id)

    if request.method == 'POST':
        # Update the task title
        task.title = request.POST['title']
        task.save()
        return redirect('mytodo')

    return render(request, 'home.html', {'task': task})
