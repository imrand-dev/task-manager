from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from accounts.models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User 
        fields = [
            "email",
            "first_name",
            "last_name",
            "password",
            "avatar"
        ]


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User 
        fields = [
            "email",
            "first_name",
            "last_name",
            "password",
            "avatar"
        ]