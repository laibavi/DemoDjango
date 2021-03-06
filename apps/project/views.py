import csv

from django.db.models import Prefetch, Sum, Q, Count, IntegerField
from datetime import datetime

from django.db.models.functions import ExtractMonth, ExtractYear, Concat, Cast
from django.shortcuts import HttpResponse
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action

from .serializers import *

# Create your views here.
from ..utils.views_helper import GenericViewSet


@method_decorator(name='update', decorator=swagger_auto_schema(auto_schema=None))
@method_decorator(name='destroy', decorator=swagger_auto_schema(auto_schema=None))
# @method_decorator(name='partial_update', decorator=swagger_auto_schema(manual_parameters=[language_swagger_query]))
class ProjectsPlansViewSet(GenericViewSet):
    queryset = Projects.objects.all()
    # serializer_class = ProjectCreateRequestSerializer
    action_serializers = {
        "create_request": ProjectCreateRequestSerializer,
        "list_response": ProjectsPlansSerializer,
        "create_response": ProjectCreateResponseSerializer,
    }

    def list(self, request, *args, **kwargs):
        current_date = datetime.datetime.now()
        self.queryset = Projects.objects.prefetch_related(
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
        return super().list(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        pass

    def destroy(self, request, *args, **kwargs):
        pass
