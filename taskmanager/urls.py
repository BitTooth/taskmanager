from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'), 										# /taskmanager/
	url(r'^(?P<task_id>[0-9]+)/$', views.detail, name='detail'),				# /taskmanager/10/
	url(r'^(?P<task_id>[0-9]+)/comments/$', views.comments, name='comments') 	# /taskmanager/10/comments
]