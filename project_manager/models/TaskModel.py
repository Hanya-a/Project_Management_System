from django.db import models
from .ProjectModel import Project
from django.contrib.auth.models import User
from .TagModel import Tag
class Task(models.Model):

    STATUS = [
            ("TODO","todo"),
            ("IN_PROGRESS","in_progress"),
            ("DONE","done")
    ]

    PRIORITY = [

        ("LOW","low"),
        ("MEDIUM","medium"),
        ("HIGH","high")
        ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20,choices=STATUS)
    priority = models.CharField(max_length=20,choices=PRIORITY)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(User,null=True,blank=True,on_delete=models.SET_NULL,related_name="assigned_tasks")
    created_by= models.ForeignKey(User, on_delete=models.CASCADE,related_name="created_tasks")
    due_date = models.DateTimeField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

