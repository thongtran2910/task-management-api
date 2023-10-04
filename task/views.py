from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Task, Member
from .serializers import TaskSerializer, MemberSerializer

# Create your views here.


@api_view(["GET"])
def task_list_serialized(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def member_list_serialized(request):
    members = Member.objects.all()
    serializer = MemberSerializer(members, many=True)
    return Response(serializer.data)
