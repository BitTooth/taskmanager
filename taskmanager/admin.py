from django.contrib import admin

from .models import Task, Comment

# Register your models here.

class CommentInline(admin.TabularInline):
	model = Comment
	extra = 1

class TaskAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields':['done', 'parent', 'name', 'description']}),
		('Date information', {'fields':['create_date', 'due_date', 'done_date']}),
	]
	inlines = [CommentInline]

admin.site.register(Task, TaskAdmin)