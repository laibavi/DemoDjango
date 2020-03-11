from django.db import models
from apps.staff.models import Staffs
from .constants import StatusType, ProjectType

STATUS = ((StatusType.CANCELED, 'Canceled'),
          (StatusType.COMPLETED, 'Completed'),
          (StatusType.INITIALIZING, 'Initializing'),
          (StatusType.INPROGRESS, 'Inprogress'),
          (StatusType.NOT_STARTED, 'Not Started'),
          (StatusType.PENDING, 'Pending'))

PROJECT_TYPE = ((ProjectType.DOMESTIC, 'Domestic'),
                (ProjectType.INTERNATIONAL, 'International'))


class Partners(models.Model):
    partner_name = models.CharField(max_length=254, null=False)
    description = models.TextField()
    status = models.IntegerField(default=1, max_length=10)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)


class Projects(models.Model):
    partner_id = models.ForeignKey(Partners, on_delete=models.CASCADE, related_name='partner', null=False)
    project_code = models.CharField(max_length=20, null=False)
    project_name = models.CharField(max_length=254, null=False)
    project_type_id = models.IntegerField(choices=PROJECT_TYPE, null=False)
    status = models.IntegerField(choices=STATUS, null=False)
    start_date = models.DateTimeField(auto_now=False)
    end_date = models.DateTimeField(auto_now=False)
    team_leader_id = models.OneToOneField(Staffs, on_delete=models.CASCADE, null=False)
    leader_id = models.OneToOneField(Staffs, on_delete=models.CASCADE, null=False)
    brse_id = models.OneToOneField(Staffs, on_delete=models.CASCADE, null=False)
    comtor_id = models.OneToOneField(Staffs, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True)


class PlanProject(models.Model):
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='project', null=False)
    plan_effort = models.FloatField()
    start_date = models.DateTimeField(auto_now=False)
    end_date = models.DateTimeField(auto_now=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)


class StaffProject(models.Model):
    staff_id = models.ForeignKey(Staffs, on_delete=models.CASCADE, related_name='staff')
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='project')
    start_date = models.DateTimeField(auto_now=False)
    end_date = models.DateTimeField(auto_now=False)
    effort = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True)
