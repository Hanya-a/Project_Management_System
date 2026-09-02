from rest_framework import viewsets
from ..models.TaskModel import Task
from ..serializers.TaskSerializer import TaskSerializer
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from django.db.models import Q

class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(Q(project__owner=self.request.user)|Q(assigned_to=self.request.user))

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_fields = ["status", "priority", "completed","project"]
    search_fields=["title"]
    ordering_fields=["created_at","due_date"]
