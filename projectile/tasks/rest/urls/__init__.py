from django.urls import path, include 

urlpatterns = [
    path("/tasks", include("tasks.rest.urls.tasks")),
    path("/tags", include("tasks.rest.urls.tags")),
]