from django.db import models
from django.utils import timezone

from autoslug import AutoSlugField

from common.base_model import BaseModelWithUID

from tasks.choices import TaskPriority

from accounts.models import User 


class Task(BaseModelWithUID):
    title = models.CharField(max_length=100)
    slug = AutoSlugField(
        populate_from="title",
        unique=True,
        unique_with="title",
    )
    created_by = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="user_tasks",
        null=True,
        blank=True,
    )
    description = models.TextField(null=True, blank=True)
    priority = models.CharField(
        max_length=7,
        choices=TaskPriority.choices,
        default=TaskPriority.LOW
    )
    due_date = models.DateField(default=timezone.now().date() + timezone.timedelta(days=5))
    is_completed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
        ordering = ["-created_at"]
    

class Photo(BaseModelWithUID):
    task = models.ForeignKey(
        to=Task,
        on_delete=models.CASCADE,
        related_name="task_photos",
        null=True,
        blank=True,
    )
    photo = models.ImageField(upload_to="photos/")
    created_by = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="user_task_photos",
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return str(self.uid)
    
    class Meta:
        verbose_name = "Photo"
        verbose_name = "Photos"
        ordering = ["-created_at"]