from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
# Create your views here.


class ProjectsPlansViewSet(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectsPlansSerializer




