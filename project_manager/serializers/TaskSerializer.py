from rest_framework import serializers
from ..models.TaskModel import Task

class TaskSerializer(serializers.ModelSerializer):
    tags=serializers.SlugRelatedField(many=True,read_only=True,slug_field="name")
    class Meta:
        model=Task
        fields=["title","description","project","status","priority","assigned_to","due_date","completed","tags"]

    def validate_project(self, project):
        if project.owner != self.context["request"].user:
            raise serializers.ValidationError(
                "You can only use projects that you own."
            )

        return project

    def validate_title(self, title):
        if title.strip()=="":
            raise serializers.ValidationError("Task title cannot be empty.")
        return title