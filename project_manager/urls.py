from .views.TaskView import TaskView
from .views.ProjectView import ProjectView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("projects", ProjectView,basename="projects")
router.register("tasks", TaskView,basename="tasks")

urlpatterns=router.urls