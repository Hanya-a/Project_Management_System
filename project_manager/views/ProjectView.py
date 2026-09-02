from rest_framework import viewsets
from ..models.ProjectModel import Project
from ..serializers.ProjectSerializer import ProjectSerializer
from rest_framework.permissions import IsAuthenticated


class ProjectView(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Project.objects.filter(owner=self.request.user)
