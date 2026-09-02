from django.contrib import admin
from .models.TagModel import Tag
from .models.TaskModel import Task
from .models.ProjectModel import Project

admin.site.register(Task)
admin.site.register(Project)
admin.site.register(Tag)

# Register your models here.
