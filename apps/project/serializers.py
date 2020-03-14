from rest_framework import serializers
from apps.project.models import *


class StaffProjectsSerializer(serializers.ModelSerializer):
    actual_effort = serializers.SerializerMethodField()

    def get_actual_effort(self, effort):
        actual_effort = 0
        for effort in self.instance:
            actual_effort += effort
        return actual_effort

    class Meta:
        model = StaffProjects
        fields = ('actual_effort',)


class PlanProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanProjects
        field = '__all__'


class PlanEffortSerialiazer(serializers.Serializer):
    month = serializers.SerializerMethodField()
    plan_effort = serializers.SerializerMethodField()
    actual_effort = serializers.SerializerMethodField()

    class Meta:
        fields = ('month', 'plan_effort', 'actual_effort')

    def get_month(self, obj):
        return obj.start_date.strftime("%m/%Y")

    def get_actual_effort(self, obj):
        return obj._actual_effort

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
