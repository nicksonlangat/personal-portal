from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
# Create your views here.


class TaskViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing task instances.
    """
    serializer_class = TaskSerializer
    queryset = Task.objects.all()