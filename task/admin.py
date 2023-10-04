from django.contrib import admin

from .models import Task, Member

# Register your models here.
admin.site.register(Task)
admin.site.register(Member)
