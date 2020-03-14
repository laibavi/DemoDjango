from django.db.models import Prefetch, Sum
from datetime import datetime

from .serializers import *
from rest_framework import viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response


# Create your views here.
class ProjectsPlansViewSet(viewsets.ModelViewSet):
    current_date = datetime.now()
    queryset = Projects.objects.prefetch_related(
        Prefetch(
            "planprojects_set",
            queryset=PlanProjects.objects.annotate(
                _actual_effort=Sum("project__staffprojects__effort")
            ).filter(start_date__month__lte=current_date.month + 1,
                     start_date__month__gte=current_date.month - 1),
            to_attr="_month_project"
        )
    )
    serializer_class = ProjectsPlansSerializer
# prefetch_related(
#                Prefetch(
#                    "project__staffprojects_set",
#                    queryset=StaffProjects.objects.annotate(_effort=Sum('effort')),
#                    to_attr="_actual_effort"
#                )
#            )
