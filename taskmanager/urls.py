from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'), 										# /taskmanager/
	url(r'^(?P<task_id>[0-9]+)/$', views.detail, name='detail'),				# /taskmanager/10/
	url(r'^(?P<task_id>[0-9]+)/comments/$', views.comments, name='comments'), 	# /taskmanager/10/comments
	url(r'^(?P<task_id>[0-9]+)/add_comment/$', views.add_comment, name='add_comment'),
	url(r'^(?P<task_id>[0-9]+)/delete_comment/(?P<comment_id>[0-9]+)/$', views.delete_comment, name='delete_comment'),
	url(r'^task_done/(?P<task_id>[0-9]+)/$', views.task_done, name='task_done'),
]