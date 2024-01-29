from django.urls import path 

from tasks.rest.views.tags import PrivateTagView, PrivateTagDetail

urlpatterns = [
    path("/<uuid:tag_uid>", PrivateTagDetail.as_view(), name="tag-detail"),
    path("", PrivateTagView.as_view(), name="tag-lists"),
]