from rest_framework import serializers
from ..models.ProjectModel import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields=["id","owner","name","description"]
        read_only_fields = ["id", "owner"]
    def validate_name(self, name):
        if name.strip()=="":
            raise serializers.ValidationError("Project name cannot be empty.")
        return name