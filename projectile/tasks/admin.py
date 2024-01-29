from django.contrib import admin
from django.utils.html import format_html

from tasks.models import Task, Photo, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["uid", "label"]
    search_fields = ["label"]
    list_per_page = 25
    autocomplete_fields = ["created_by"]


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "due_date",
        "priority",
        "status",
        "duration",
        "created_at",
    ]
    search_fields = ["title"]
    list_editable = ["due_date"]
    list_per_page = 25
    list_filter = [
        "priority",
        "due_date",
        "status",
    ]
    autocomplete_fields = ["created_by"]


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = [
        "uid",
        "task_title",
        "display_photo",
    ]
    list_per_page = 20
    list_select_related = ["task"]
    autocomplete_fields = ["task", "created_by"]

    def display_photo(self, instance):
        return format_html(
            '<img src="{}" width="75" height="90"/>', instance.photo.url
        )

    def task_title(self, instance):
        return instance.task.title
