from rest_framework.generics import (
    get_object_or_404,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated

from tasks.models import Tag 
from tasks.rest.serializers.tags import TagSerializer


class PrivateTagView(ListCreateAPIView):
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Tag.objects.filter(created_by=user)
    

class PrivateTagDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "patch", "delete"]

    def get_object(self):
        user = self.request.user 
        tag_uid = self.kwargs.get("tag_uid", None)

        return get_object_or_404(queryset=Tag, created_by=user, uid=tag_uid)
