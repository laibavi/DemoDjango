from datetime import datetime

from dateutil.relativedelta import relativedelta
from rest_framework import serializers

from apps.staff.models import Staffs, Groups
from apps.project.models import StaffProjects, Projects


class ProjectsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Projects
        fields = ['id', 'project_name']


class StaffProjectSerializer(serializers.ModelSerializer):
    project = serializers.SerializerMethodField()

    class Meta:
        model = StaffProjects
        fields = ['project', 'effort']

    def get_project(self, obj):
        return ProjectsSerializer(obj.project).data


class StaffsSerializer(serializers.ModelSerializer):
    efforts = serializers.SerializerMethodField()

    class Meta:
        model = Staffs
        fields = ['id', 'staff_code', 'full_name', 'efforts']

    def get_efforts(self, obj):
        arr = []
        current_time = datetime.now()
        time = datetime.strptime(current_time.strftime('%m/%Y'), '%m/%Y') - relativedelta(months=1)
        for month in range(current_time.month - 1, current_time.month + 2):
            staffProjects = []

            for item in obj._effort:
                if month == item.start_date.month:
                    staffProjects.append(item)

            arr.append({
                "month": time.strftime('%m/%Y'),
                "project_staff": StaffProjectSerializer(staffProjects, many=True).data
            })
            time += relativedelta(months=1)
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

    def get_group_lead(self, obj):
        if hasattr(obj, '_group_leader'):
            return StaffsSerializer1(obj._group_leader[0]).data
        else:
            return None

    def get_staffs(self, obj):
        return StaffsSerializer(obj._staffs, many=True).data


class StaffCreateRequestSerializer(serializers.ModelSerializer):
    month = serializers.CharField(required=True)

    class Meta:
        model = StaffProjects
        fields = ['month', 'staff', 'project', 'effort']

    def save(self, **kwargs):
        month = self.validated_data["month"]
        start_date = datetime.strptime(month, '%m/%Y')
        end_date = start_date + relativedelta(months=1) - relativedelta(days=1)
        instance = StaffProjects.objects.filter(start_date=start_date, end_date=end_date)
        if instance.exists():
            instance = instance.first()
            instance.effort = self.validated_data["effort"]
            instance.save()
            return instance
        else:
            instance = StaffProjects.objects.create(
                staff=self.validated_data["staff"],
                project=self.validated_data["project"],
                effort=self.validated_data["effort"],
                start_date=start_date,
                end_date=end_date
            )
            return instance


class StaffCreateResponseSerializer(serializers.ModelSerializer):
    month = serializers.SerializerMethodField()

    class Meta:
        model = StaffProjects
        fields = ['month', 'staff', 'project', 'effort']

    def get_month(self, obj):
        return obj.start_date.strftime('%m/%Y')

# class ExportCSVResponseSerializer(serializers.ModelSerializer):

