from django.db.models import Prefetch
from django.shortcuts import render
from rest_framework import viewsets

from apps.project.models import Projects, StaffProject


class ProjectsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Projects.objects.all()

