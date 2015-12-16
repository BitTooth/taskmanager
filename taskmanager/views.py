from django.shortcuts import get_object_or_404, render

from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.utils import timezone

from .models import Task, Comment

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

def add_comment(request, task_id):
	task = get_object_or_404(Task, pk=task_id)
	content = request.POST['content']
	comment = Comment()
	comment.content = content
	comment.task = task
	comment.save()
	return HttpResponseRedirect(reverse('detail', args=(task.id,)))

def delete_comment(request, task_id, comment_id):
	comment = get_object_or_404(Comment, pk=comment_id)
	task = get_object_or_404(Task, pk=task_id)
	comment.delete()
	return HttpResponseRedirect(reverse('detail', args=(task.id,)))

def task_done(request, task_id):
	task = get_object_or_404(Task, pk=task_id)
	task.done = not task.done
	task.save()
	return HttpResponseRedirect(reverse('index'))

def new_task(request, task_id):
	task = get_object_or_404(Task, pk=task_id)
	print 'trying to create task for subtask ', task_id
	return render(request, 'taskmanager/new_task.html', {'task':task})

def add_task(request, task_id):
	parent_task = get_object_or_404(Task, pk=task_id)
	new_task = Task()
	new_task.parent = parent_task
	new_task.name = request.POST['name']
	new_task.description = request.POST['content']
	new_task.create_date = timezone.now()
	new_task.save()
	return HttpResponseRedirect(reverse('index'))	

def edit_description(request, task_id):
	task = get_object_or_404(Task, pk=task_id)
	task.description = request.POST['name']
	task.save()
	return HttpResponseRedirect(reverse('detail', args=(task.id,)))
