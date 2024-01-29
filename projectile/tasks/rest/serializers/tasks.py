from datetime import date

from django.utils import timezone 

from rest_framework import serializers
from rest_framework.exceptions import NotFound

from tasks.models import Task, Photo, Tag
from tasks.rest.serializers.tags import TagSerializer 
from tasks.rest.serializers.photos import PhotoSerializer


class TaskSerializer(serializers.ModelSerializer):
    tag_uids = serializers.ListField(
        child=serializers.UUIDField(), 
        required=False,
        write_only=True,
    )
    added_tags = serializers.ListField(
        child=serializers.CharField(), 
        required=False,
        write_only=True, 
    )
    task_photos = PhotoSerializer(many=True, read_only=True, required=False)
    uploaded_photos = serializers.ListField(
        child=serializers.ImageField(
            allow_empty_file=False,
            use_url=False,
        ),
        write_only=True,
        required=False,
    )

    class Meta:
        model = Task 
        fields = [
            "uid",
            "slug",
            "title",
            "status",
            "priority",
            "due_date",
            "duration",
            "tag_uids",
            "added_tags",
            "created_at",
            "updated_at",
            "description",
            "task_photos",
            "uploaded_photos",
        ]
        read_only_fields = [
            "uid",
            "slug",
            "created_at",
            "updated_at",
        ]
    
    def validate(self, attrs) -> dict:
        default_date = timezone.now().date() + timezone.timedelta(days=5)
        due_date = attrs.get("due_date", default_date)

        if due_date < timezone.now().date():
            raise serializers.ValidationError("Due date can't be in the past.")
        
        tag_uids = attrs.pop("tag_uids", [])
        tags = []
        for tag_uid in tag_uids:
            try:
                tag = Tag.objects.get(uid=tag_uid)
            except Tag.DoesNotExist:
                raise NotFound(detail="Tag doesn't exist")
            else:
                tags.append(tag)
        
        attrs["tags"] = tags
        return attrs
    
    def to_representation(self, instance):
        self.fields['tags'] = TagSerializer(many=True, read_only=True)
        return super().to_representation(instance)

    def create(self, validated_data):
        user = self.context["request"].user 
        uploaded_photos = validated_data.pop("uploaded_photos", [])
        tags = validated_data.pop("tags", [])
        new_tags = validated_data.pop("added_tags", [])

        if new_tags:
            for name in new_tags:
                tag = Tag.objects.create(label=name, created_by=user)
                tags.append(tag)

        task = Task.objects.create(created_by=user, **validated_data)

        task.tags.set(tags)

        for photo in uploaded_photos:
            task_photo = Photo.objects.create(
                created_by=user,
                task=task,
                photo=photo
            )
        
        return task