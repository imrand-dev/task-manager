from django.urls import path, include 

urlpatterns = [
    path("", include("tasks.rest.urls.tasks"))
]