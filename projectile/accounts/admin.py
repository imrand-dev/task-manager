from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from accounts.forms import CustomUserCreationForm, CustomUserChangeForm
from accounts.models import User 


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ["first_name", "last_name", "email", "is_staff"]
    search_fields = ["email"]
    ordering = ["-email"]
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    # update the existing user
    fieldsets = (
        (None, {
            "fields": [
                "email", 
                "password"
            ]
        }),
        ("Personal Info", {
            "fields": [
                "first_name",
                "last_name",
                "avatar"
            ]
        }),
        ("Permissions", {
            "fields": [
                "is_staff",
                "is_active",
                "is_verified",
                "is_superuser",
                "groups", 
                "user_permissions"
            ]
        }),
        ("Important dates", {
            "fields": [
                "last_login",
            ]
        })
    )

    # create a new user
    add_fieldsets = (
        (None, {
            "classes": ["wide",],
            "fields": [
                "first_name",
                "last_name",
                "email",
                "password1",
                "password2",
                "avatar"
            ]
        }),
    )





