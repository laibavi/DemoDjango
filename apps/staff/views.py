import csv
from datetime import datetime

from django.db.models import Prefetch
from django.db.models.functions import TruncMonth
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema

from rest_framework import viewsets, permissions
from rest_framework.decorators import action

from apps.project.models import Projects, StaffProjects
from apps.staff.models import Staffs, Groups
from apps.staff.serializers import StaffsSerializer1, GroupsSerializer, StaffsSerializer, StaffCreateRequestSerializer, \
    StaffCreateResponseSerializer
from apps.utils.views_helper import GenericViewSet


@method_decorator(name='update', decorator=swagger_auto_schema(auto_schema=None))
@method_decorator(name='destroy', decorator=swagger_auto_schema(auto_schema=None))
class StaffViewSet(GenericViewSet):
    queryset = Groups.objects.all()
    action_serializers = {
        "list_response": GroupsSerializer,
        "create_request": StaffCreateRequestSerializer,
        "create_response": StaffCreateResponseSerializer,
        # "exportCSV_response": ExportCSVResponseSerializer,
    }

    def list(self, request, *args, **kwargs):
        current_date = datetime.now()
        self.queryset = Groups.objects.prefetch_related(
            Prefetch(
                "staffs_set",
                queryset=Staffs.objects.filter(position_id__position_name="group leader"),
                to_attr="_group_leader"
            ),
            Prefetch(
                "staffs_set",
                queryset=Staffs.objects.prefetch_related(
                    Prefetch(
                        'staffprojects_set',
                        queryset=StaffProjects.objects.filter(
                            start_date__month__lte=current_date.month + 1,
                            start_date__month__gte=current_date.month - 1
                        ).annotate(
                            month=TruncMonth('start_date')  # Truncate to month and add to select list
                        ),
                        to_attr="_effort"
                    )
                ),
                to_attr="_staffs"
            )
        )
        return super().list(request)

    def update(self, request, *args, **kwargs):
        pass

    @action(detail=False, methods=['get', ], url_path='export-data')
    def export_data(self, request, *args, **kwargs):
        current_month = datetime.now().strftime('%m/%Y')
        previous_month = current_month-1
        next_month = current_month+1
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="staffs.csv"'

        writer = csv.writer(response)
        writer.writerow([
            'STT',
            'CODE',
            'NAME',
            previous_month,
            current_month,
            next_month,
            'Action'
        ])

        return response

