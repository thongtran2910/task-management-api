from django.urls import path
from .views import task_list_serialized, member_list_serialized

urlpatterns = [
    path("api/task-list", task_list_serialized),
    path("api/member-list", member_list_serialized),
]
