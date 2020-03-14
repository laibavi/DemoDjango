from .constants import *
from django.db import models


WORKINGS = (
    (WorkingType.FULL_TIME.value, 'Full Time'),
    (WorkingType.PART_TIME.value, 'Part Time'),
)

LANGUAGES = (
    (LanguageType.ENGLISH.value, 'English'),
    (LanguageType.JAPANESE.value, 'Japanese'),
    (LanguageType.FRENCH.value, 'French'),
)


class DeveloperTypes(models.Model):
    name = models.CharField(max_length=255)
    status = models.BooleanField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'developer_types'

    def __str__(self):
        return self.name


class Groups(models.Model):
    group_name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.BooleanField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'groups'

    def __str__(self):
        return self.group_name


class Ranks(models.Model):
    rank_name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.BooleanField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'ranks'

    def __str__(self):
        return self.rank_name


class Positions(models.Model):
    position_name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.BooleanField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'positions'

    def __str__(self):
        return self.position_name


class Staffs(models.Model):
    developer_type = models.ForeignKey(DeveloperTypes, on_delete=models.CASCADE, blank=True)
    rank = models.ForeignKey(Ranks, on_delete=models.CASCADE, blank=True)
    position = models.ForeignKey(Positions, on_delete=models.CASCADE, blank=True)
    group = models.ForeignKey(Groups, on_delete=models.CASCADE)
    working_type_id = models.IntegerField(choices=WORKINGS)
    staff_code = models.CharField(max_length=20)
    full_name = models.CharField(max_length=255)
    note = models.TextField(blank=True)
    experience_from = models.DateTimeField(blank=True)
    status = models.BooleanField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'staffs'

    def __str__(self):
        return self.full_name


class Languages(models.Model):
    staff = models.ForeignKey(Staffs, on_delete=models.CASCADE)
    language_id = models.IntegerField(choices=LANGUAGES, blank=True)

    class Meta:
        db_table = 'languages'


class Skills(models.Model):
    skill_name = models.CharField(max_length=255)
    status = models.BooleanField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'skills'

    def __str__(self):
        return self.skill_name


class StaffSkills(models.Model):
    staff = models.ForeignKey(Staffs, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skills, on_delete=models.CASCADE)
    status = models.BooleanField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'staff_skills'








