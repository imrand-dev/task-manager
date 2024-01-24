from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from accounts.forms import CustomUserCreationForm, CustomUserChangeForm
from accounts.models import User 


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ["first_name", "last_name", "email", "is_superuser"]
    search_fields = ["email"]
    ordering = ["-email"]
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    # update the user form
    fieldsets = (
        (None, {
            "fields": [
                "email", 
                "password"
            ]
        }),
        ("Profile", {
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
            ]
        }),
        ("Groups and Permisions", {
            "fields": [
                "groups", 
                "user_permissions"
            ]
        }),
    )

    # create a new user form
    add_fieldsets = (
        (None, {
            "classes": ["wide"],
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





