from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class Task(models.Model):
    PRIORITY_CHOICES = (
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High"),
    )

    priority = models.CharField(max_length=50, choices=PRIORITY_CHOICES)
    title = models.CharField(max_length=150)
    description = models.TextField()
    date_posted = models.DateField(null=True)
    deadline = models.DateField(null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")
    img = models.ImageField(upload_to="tasks", blank=True, null=True)

    def __str__(self):
        return f"{self.title} | {self.priority}"


class Member(models.Model):
    name = models.CharField(max_length=100)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="members")
    avatar = models.ImageField(upload_to="members", blank=True, null=True)

    def __str__(self):
        return f"{self.name} | {self.task}"
