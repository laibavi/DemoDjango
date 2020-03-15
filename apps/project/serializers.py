import calendar
import datetime

from dateutil.relativedelta import relativedelta
from rest_framework import serializers
from apps.project.models import *


class PlanEffortSerialiazer(serializers.Serializer):
    month = serializers.SerializerMethodField()
    plan_effort = serializers.SerializerMethodField()
    actual_effort = serializers.SerializerMethodField()

    class Meta:
        fields = ('month', 'plan_effort', 'actual_effort')

    def get_month(self, obj):
        return obj.start_date.strftime("%m/%Y")

    def get_actual_effort(self, obj):
        if obj._actual_effort:
            return obj._actual_effort
        return 0

    def get_plan_effort(self, obj):
        return obj.plan_effort


class ProjectsPlansSerializer(serializers.ModelSerializer):
    efforts = serializers.SerializerMethodField()

    class Meta:
        model = Projects
        fields = ('id', 'project_code', 'project_name', 'efforts')

    def get_efforts(self, obj):
        if hasattr(obj, "_month_project"):
            return PlanEffortSerialiazer(obj._month_project, many=True).data
        return None


class ProjectCreateRequestSerializer(serializers.ModelSerializer):
    month = serializers.CharField(required=True)

    class Meta:
        model = PlanProjects
        fields = ('month', 'project', 'plan_effort')

    def validate_plan_effort(self, value):
        return value

    def save(self, **kwargs):
        # check db co hay ko roi moi tao
        month = self.validated_data["month"]
        start_date = datetime.datetime.strptime(month, '%m/%Y')
        end_date = start_date + relativedelta(months=1) - relativedelta(days=1)
        instance = PlanProjects.objects.filter(start_date=start_date, end_date=end_date)
        if instance.exists():
            instance = instance.first()
            instance.plan_effort = self.validated_data["plan_effort"]
            instance.save()
            return instance
        else:
            instance = PlanProjects.objects.create(
                project=self.validated_data["project"],
                plan_effort=self.validated_data["plan_effort"],
                start_date=start_date, end_date=end_date)
            return instance


class ProjectCreateResponseSerializer(serializers.ModelSerializer):
    month = serializers.SerializerMethodField()
    class Meta:
        model = PlanProjects
        fields = ('id', 'month', 'plan_effort')

    def get_month(self, obj):
        return obj.start_date.strftime("%m/%Y")