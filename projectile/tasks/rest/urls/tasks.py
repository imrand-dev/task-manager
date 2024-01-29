from django.urls import path 

from tasks.rest.views.tasks import PrivateTaskView, PrivateTaskDetail

urlpatterns = [
    path("/<uuid:task_uid>", PrivateTaskDetail.as_view(), name="task-detail"),
    path("", PrivateTaskView.as_view(), name="task-lists")
]