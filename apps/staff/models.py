from .constants import *

from django.db import models


WORKINGS = ((WorkingType.FULL_TIME, 'Full time'),
            (WorkingType.PART_TIME, 'Part time'))

LANGUAGES = ((LanguageType.ENGLISH, 'English'),
             (LanguageType.JAPANESE, 'Japanese'),
             (LanguageType.FRENCH, 'French'),)


class DeveloperType(models.Model):
    name = models.CharField(max_length=255)
    status = models.IntegerField(default=1, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)


class Groups(models.Model):
    group_name = models.CharField(max_length=255, null=False)
    description = models.TextField()
    status = models.IntegerField(default=1, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)


class Ranks(models.Model):
    rank_name = models.CharField(max_length=255)
    description = models.TextField()
    status = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)


class Positions(models.Model):
    position_name = models.CharField(max_length=254)
    description = models.TextField()
    status = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)


class Staffs(models.Model):
    developer_type_id = models.ForeignKey(DeveloperType, on_delete=models.CASCADE)
    rank_id = models.ForeignKey(Ranks, on_delete=models.CASCADE)
    position_id = models.ForeignKey(Positions, on_delete=models.CASCADE)
    group_id = models.ForeignKey(Groups, on_delete=models.CASCADE)
    working_type_id = models.IntegerField(choices=WORKINGS, null=False)
    staff_code = models.CharField(max_length=20, null=False)
    full_name = models.CharField(max_length=254, null=False)
    note = models.TextField()
    experience = models.FloatField()
    status = models.IntegerField(default=1, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)


class Languages(models.Model):
    staff_id = models.ForeignKey(Staffs, on_delete=models.CASCADE)
    language_id = models.IntegerField(choices=LANGUAGES)


class Skills(models.Model):
    skill_name = models.CharField(max_length=254, null=False)
    status = models.BooleanField(default=1, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)


class StaffSkill(models.Model):
    staff_id = models.ForeignKey(Staffs, on_delete=models.CASCADE)
    skill_id = models.ForeignKey(Skills, on_delete=models.CASCADE)
    status = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)








