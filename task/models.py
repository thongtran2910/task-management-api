from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class Task(models.Model):
    PRIORITY_CHOICES =  (
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    )

    priority = models.CharField(max_length=50, choices=PRIORITY_CHOICES)
    title = models.CharField(max_length=150)
    description = models.TextField()
    date_posted = models.DateField(null=True)
    deadline = models.DateField(null=True)
    owner = models.ForeignKey()