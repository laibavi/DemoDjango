from django.db.models import Prefetch, Sum, Q
from datetime import datetime

from django.db.models.functions import ExtractMonth, ExtractYear
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema

from .serializers import *
from rest_framework import viewsets


# Create your views here.
@method_decorator(name='update', decorator=swagger_auto_schema(auto_schema=None))
class ProjectsPlansViewSet(viewsets.ModelViewSet):
    current_date = datetime.now()
    queryset = Projects.objects.prefetch_related(
        Prefetch(
            "planprojects_set",
            queryset=PlanProjects.objects.annotate(
                _actual_effort=Sum("project__staffprojects__effort",
                                   filter=Q(project__staffprojects__start_date__month=ExtractMonth('start_date')) &
                                          Q(project__staffprojects__start_date__year=ExtractYear('start_date')))
            ).filter(start_date__month__lte=current_date.month + 1,
                     start_date__month__gte=current_date.month - 1),
            to_attr="_month_project"
        )
    )
    serializer_class = ProjectsPlansSerializer
