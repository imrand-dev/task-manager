from rest_framework import serializers

from tasks.models import Photo


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = [
            "uid",
            "task",
            "photo",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "uid",
            "created_at",
            "updated_at",
        ]
    
    def create(self, validated_data):
        user = self.context["request"].user 
        photo = validated_data.get("photo")
        task = validated_data.get("task")

        return Photo.objects.create(
            created_by=user,
            task=task,
            photo=photo,
        )
