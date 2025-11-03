from django.shortcuts import render
from rest_framework import viewsets
from taskmanager.models import Task
from taskmanager.serializers import TaskSerializer

# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-id')
    serializer_class = TaskSerializer

