from django.db import models
from apps.staff.models import Staffs
from .constants import StatusType, ProjectType

STATUS = (
    (StatusType.CANCELED.value, 'Canceled'),
    (StatusType.COMPLETED.value, 'Completed'),
    (StatusType.INITIALIZING.value, 'Initializing'),
    (StatusType.INPROGRESS.value, 'Inprogress'),
    (StatusType.NOT_STARTED.value, 'Not Started'),
    (StatusType.PENDING.value, 'Pending'),
)

PROJECT_TYPE = (
    (ProjectType.DOMESTIC.value, 'Domestic'),
    (ProjectType.INTERNATIONAL.value, 'International'),
)


class Partners(models.Model):
    partner_name = models.CharField(max_length=254)
    description = models.TextField(blank=True)
    status = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'partners'

    def __str__(self):
        return self.partner_name


class Projects(models.Model):
    partner_id = models.ForeignKey(Partners, on_delete=models.CASCADE)
    project_code = models.CharField(max_length=20)
    project_name = models.CharField(max_length=254)
    project_type_id = models.IntegerField(choices=PROJECT_TYPE)
    status = models.IntegerField(choices=STATUS)
    start_date = models.DateTimeField(auto_now=False)
    end_date = models.DateTimeField(auto_now=False, blank=True)
    team_leader_id = models.OneToOneField(Staffs, on_delete=models.CASCADE, related_name="team_leader_staff")
    leader_id = models.OneToOneField(Staffs, on_delete=models.CASCADE, related_name="leader_staff")
    brse_id = models.OneToOneField(Staffs, on_delete=models.CASCADE, related_name="brse_staff")
    comtor_id = models.OneToOneField(Staffs, on_delete=models.CASCADE, related_name="comtor_staff")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'projects'

    def __str__(self):
        return self.project_name


class PlanProject(models.Model):
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE)
    plan_effort = models.FloatField(blank=True)
    start_date = models.DateTimeField(auto_now=False)
    end_date = models.DateTimeField(auto_now=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'plan_project'


class StaffProject(models.Model):
    staff_id = models.ForeignKey(Staffs, on_delete=models.CASCADE)
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now=False)
    end_date = models.DateTimeField(auto_now=False, blank=True)
    effort = models.FloatField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'staff_project'
