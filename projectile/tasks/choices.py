from django.db import models


class TaskPriority(models.TextChoices):
    LOW = "Low", "Low"
    HIGH = "High", "High"
    MEDIUM = "Medium", "Medium"