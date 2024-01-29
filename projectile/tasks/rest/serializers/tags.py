from rest_framework import serializers

from tasks.models import Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            "uid",
            "slug",
            "label",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "uid",
            "slug",
            "created_at",
            "updated_at",
        ]
    
    def create(self, validated_data):
        user = self.context["request"].user
        label = self.validated_data.get("label", "")

        return Tag.objects.create(
            created_by=user,
            label=label,
        )