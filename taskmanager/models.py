from django.db import models

# Create your models here.

class Task(models.Model):
	parent 			= models.ForeignKey('self', null=True, blank=True)
	name 			= models.CharField(max_length=200)
	description 	= models.TextField(max_length=1024)
	create_date 	= models.DateTimeField('creation date')
	due_date 		= models.DateTimeField('due date', blank=True, null=True)
	done_date 		= models.DateTimeField('done date', blank=True, null=True)
	done 			= models.BooleanField(default=False)

	def __unicode__(self):
		return self.name

class Comment(models.Model):
	task 		= models.ForeignKey(Task)
	content 	= models.TextField(max_length=2048)

	def __unicode__(self):
		return self.content