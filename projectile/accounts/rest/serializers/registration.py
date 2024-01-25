from rest_framework import serializers

from accounts.models import User
from accounts.services.users import UserService


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        style={
            "input_type": "password",
        },
        source="password1",
        max_length=32,
        min_length=6,
    )
    confirm_password = serializers.CharField(
        write_only=True,
        style={
            "input_type": "password",
        },
        source="password2",
        max_length=32,
        min_length=6,
    )

    class Meta:
        model = User
        fields = [
            "uid",
            "created_at",
            "updated_at",
            "first_name",
            "last_name",
            "slug",
            "email",
            "password",
            "confirm_password",
            "avatar",
            "is_active",
            "is_staff",
            "is_verified",
        ]
        read_only_fields = [
            "uid",
            "slug",
            "created_at",
            "updated_at",
            "is_active",
            "is_staff",
            "is_verified",
        ]

    def validate(self, attrs):
        password1 = attrs.get("password1")
        password2 = attrs.get("password2")

        if password1 != password2:
            raise serializers.ValidationError({"password": "Password doesn't match."})
        
        return attrs

    def create(self, validated_data):
        user_service = UserService()
        return user_service.create_user(**validated_data)
