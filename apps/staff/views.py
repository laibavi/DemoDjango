from datetime import datetime

from django.db.models import Prefetch
from django.db.models.functions import TruncMonth
from django.shortcuts import render

from rest_framework import viewsets, permissions

from apps.project.models import Projects, StaffProject
from apps.staff.models import Staffs, Groups
from apps.staff.serializers import StaffsSerializer1, GroupsSerializer, StaffsSerializer
from apps.utils.views_helper import GenericViewSet


class StaffViewSet(GenericViewSet):
    current_date = datetime.now()
    queryset = Groups.objects.prefetch_related(
        Prefetch(
            "staffs_set",
            queryset=Staffs.objects.filter(position_id__position_name="group leader"),
            to_attr="_group_leader"
        ),
        Prefetch(
            "staffs_set",
            queryset=Staffs.objects.prefetch_related(
                Prefetch(
                    'staffproject_set',
                    queryset=StaffProject.objects.filter(
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
    serializer_class = GroupsSerializer


class StaffViewSet1(viewsets.ReadOnlyModelViewSet):
    queryset = Staffs.objects.all()
    serializer_class = StaffsSerializer


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Groups.objects.all()
    serializer_class = GroupsSerializer
    permission_classes = [permissions.IsAuthenticated]
