from .constants import *

from django.db import models


WORKINGS = ((WorkingType.Full_time, 'Full time'),
            (WorkingType.Part_time, 'Part time'))

LANGUAGES = ((LanguageType.English, 'English'),
             (LanguageType.Japanese, 'Japanese'),
             (LanguageType.French, 'French'),)


class DeveloperType(models.Model):
    name = models.CharField(max_length=255)
    status = models.IntegerField(default=1, max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField()


class Groups(models.Model):
    group_name = models.CharField(max_length=255)
    description = models.TextField()
    status = models.IntegerField(default=1, max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)


class Ranks(models.Model):
    rank_name = models.CharField(max_length=255)
    description = models.TextField()
    status = models.IntegerField(default=1, max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)


class Positions(models.Model):
    position_name = models.CharField(max_length=254)
    description = models.TextField()
    status = models.IntegerField(default=1, max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)


class Staffs(models.Model):
    developer_type_id = models.ForeignKey(DeveloperType, on_delete=models.CASCADE, related_name="developer", max_length=10)
    rank_id = models.ForeignKey(Ranks, on_delete=models.CASCADE, related_name="rank", max_length=10)
    position_id = models.ForeignKey(Positions, on_delete=models.CASCADE, related_name="position", max_length=10)
    group_id = models.ForeignKey(Groups, on_delete=models.CASCADE, related_name="group", max_length=10)
    working_type_id = models.IntegerField(choices=WorkingType)
    staff_code = models.CharField(max_length=20)
    full_name = models.CharField(max_length=254)
    note = models.TextField()
    experience = models.FloatField()
    status = models.IntegerField(default=1, max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField()


class Languages(models.Model):
    staff_id = models.ForeignKey(Staffs, on_delete=models.CASCADE, related_name='staff', max_length=10)
    language = models.IntegerField(choices=LANGUAGES)


class Skills(models.Model):
    skill_name = models.CharField(max_length=254)
    status = models.BooleanField(default=1, max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)


class StaffSkill(models.Model):
    staff_id = models.ForeignKey(Staffs, on_delete=models.CASCADE, related_name='staff', max_length=10)
    skill_id = models.ForeignKey(Skills, on_delete=models.CASCADE, related_name='skill', max_length=10)
    status = models.IntegerField(default=1, max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)








