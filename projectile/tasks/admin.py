from django.contrib import admin
from django.utils.html import format_html

from tasks.models import Task, Photo


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "due_date",
        "priority",
        "created_at",
        "is_completed",
    ]
    search_fields = ["title"]
    list_editable = ["due_date"]
    list_per_page = 20
    list_filter = [
        "priority",
        "due_date",
        "created_at",
        "is_completed",
    ]


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = [
        "uid",
        "display_photo",
        "task_title",
    ]
    list_per_page = 20
    list_select_related = ["task"]

    def display_photo(self, instance):
        return format_html(
            '<img src="{}" width="75" height="90">', instance.photo.url
        )

    def task_title(self, instance):
        return instance.task.title
