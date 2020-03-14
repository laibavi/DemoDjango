from rest_framework import serializers

from apps.project.models import Projects


class ProjectsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Projects
        fields = ['id', "project_name"]