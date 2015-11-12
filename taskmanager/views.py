from django.shortcuts import get_object_or_404, render

from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

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