from django.shortcuts import get_object_or_404, render

from .models import Task

# Create your views here.
def index(request):
	tasks = Task.objects.order_by('-create_date').reverse()
	context = { 'tasks':tasks }
	return render(request, 'taskmanager/index.html', context)

def detail(request, task_id):
	task = get_object_or_404(Task, pk=task_id)
	return render(request, 'taskmanager/detail.html', {'task':task})

def comments(request, task_id):
	return HttpResponse("Task comments page. Not implemented yet")
