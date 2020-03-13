from rest_framework import serializers
from apps.project.models import *


class PlanProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = PlanProject
        fields = ('plan_effort', )


class StaffProjectSerializer(serializers.ModelSerializer):
    actual_effort = serializers.SerializerMethodField()

    def get_actual_effort(self, effort):
        actual_effort = 0
        for effort in self.instance:
            actual_effort += effort
        return actual_effort

    class Meta:
        model = StaffProject
        fields = ('actual_effort', )


class ProjectsPlansSerializer(serializers.ModelSerializer):
    efforts = serializers.SerializerMethodField()
    plan_effort = PlanProjectSerializer(many=True)
    actual_effort = StaffProjectSerializer(many=True, read_only=True)

    def get_efforts(self,):
        a = {}

    class Meta:
        model = Projects
        fields = ('id', 'project_code', 'project_name', 'efforts', 'plan_effort', 'actual_effort')