from datetime import date

from django.utils import timezone 

from rest_framework import serializers

from tasks.models import Task, Photo


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


class TaskSerializer(serializers.ModelSerializer):
    task_photos = PhotoSerializer(many=True, read_only=True)
    uploaded_photos = serializers.ListField(
        child=serializers.ImageField(
            allow_empty_file=False,
            use_url=False,
        ),
        write_only=True,
    )

    class Meta:
        model = Task 
        fields = [
            "uid",
            "slug",
            "title",
            "due_date",
            "priority",
            "created_at",
            "updated_at",
            "description",
            "task_photos",
            "is_completed",
            "uploaded_photos",
        ]
        read_only_fields = [
            "uid",
            "slug",
            "created_at",
            "updated_at",
        ]
    
    def validate_due_date(self, due_date) -> date:
        if due_date < timezone.now().date():
            raise serializers.ValidationError("Due date can't be in the past.")

        return due_date

    def create(self, validated_data):
        user = self.context["request"].user 
        uploaded_photos = validated_data.pop("uploaded_photos")
        task = Task.objects.create(created_by=user, **validated_data)

        print(validated_data)

        for photo in uploaded_photos:
            task_photo = Photo.objects.create(
                created_by=user,
                task=task,
                photo=photo
            )
        
        return task
