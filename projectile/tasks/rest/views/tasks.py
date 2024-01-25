from rest_framework.generics import (
    get_object_or_404,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework.permissions import IsAuthenticated

from tasks.models import Task
from tasks.rest.serializers.tasks import TaskSerializer


class PrivateTaskView(ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user 
        return Task.objects.filter(created_by=user)
    

class PrivateTaskDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "patch", "delete"]

    def get_object(self):
        user = self.request.user 
        task_uid = self.kwargs.get("task_uid", None)

        return get_object_or_404(queryset=Task, uid=task_uid, created_by=user)