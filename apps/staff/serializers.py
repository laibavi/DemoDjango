from datetime import datetime

from rest_framework import serializers

from apps.project.serializers import ProjectsSerializer
from apps.staff.models import Staffs, Groups
from apps.project.models import StaffProject, Projects


class StaffProjectSerializer(serializers.ModelSerializer):
    project_id = serializers.SerializerMethodField()

    class Meta:
        model = StaffProject
        fields = ['project_id', 'effort']

    def get_project_id(self, obj):
        return ProjectsSerializer(obj.project_id).data


class StaffsSerializer(serializers.ModelSerializer):
    efforts = serializers.SerializerMethodField()

    class Meta:
        model = Staffs
        fields = ['id', 'staff_code', 'full_name', 'efforts']

    def get_efforts(self, obj):
        arr = []
        current_month = datetime.now().month
        for month in range(current_month - 1, current_month + 2):
            staffProjects = []
            for item in obj._effort:
                if month == item.start_date.month:
                    staffProjects.append(item)

            arr.append({
                "month": month,
                "project_staff": StaffProjectSerializer(staffProjects, many=True).data
            })
        return arr


class StaffsSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Staffs
        fields = ['id', 'staff_code', 'full_name']


class GroupsSerializer(serializers.ModelSerializer):
    group_lead = serializers.SerializerMethodField()
    staffs = serializers.SerializerMethodField()

    class Meta:
        model = Groups
        fields = ['id', 'group_name', 'group_lead', 'staffs']
