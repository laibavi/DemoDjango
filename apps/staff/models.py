from enum import Enum
from django.db import models


class WorkingType(Enum):
    FULL_TIME = 1
    PART_TIME = 2


class LanguageType(Enum):
    ENGLISH = 1
    JAPANESE = 2
    FRENCH = 3


WORKINGS = (
    (WorkingType.FULL_TIME.value, 'Full Time'),
    (WorkingType.PART_TIME.value, 'Part Time'),
)

LANGUAGES = (
    (LanguageType.ENGLISH.value, 'English'),
    (LanguageType.JAPANESE.value, 'Japanese'),
    (LanguageType.FRENCH.value, 'French'),
)


class DeveloperType(models.Model):
    name = models.CharField(max_length=255)
    status = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'developer_type'

    def __str__(self):
        return self.name


class Groups(models.Model):
    group_name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.IntegerField(default=1)
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
    status = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'ranks'

    def __str__(self):
        return self.rank_name


class Positions(models.Model):
    position_name = models.CharField(max_length=254)
    description = models.TextField(blank=True)
    status = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'positions'

    def __str__(self):
        return self.position_name


class Staffs(models.Model):
    developer_type_id = models.ForeignKey(DeveloperType, on_delete=models.CASCADE)
    rank_id = models.ForeignKey(Ranks, on_delete=models.CASCADE)
    position_id = models.ForeignKey(Positions, on_delete=models.CASCADE)
    group_id = models.ForeignKey(Groups, on_delete=models.CASCADE)
    working_type_id = models.IntegerField(choices=WORKINGS, default='Full Time')
    staff_code = models.CharField(max_length=20)
    full_name = models.CharField(max_length=254)
    note = models.TextField(blank=True)
    experience_from = models.DateTimeField(blank=True)
    status = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'staffs'

    def __str__(self):
        return self.full_name


class Languages(models.Model):
    staff_id = models.ForeignKey(Staffs, on_delete=models.CASCADE)
    language_id = models.IntegerField(choices=LANGUAGES)

    class Meta:
        db_table = 'languages'


class Skills(models.Model):
    skill_name = models.CharField(max_length=254)
    status = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'skills'

    def __str__(self):
        return self.skill_name


class StaffSkill(models.Model):
    staff_id = models.ForeignKey(Staffs, on_delete=models.CASCADE)
    skill_id = models.ForeignKey(Skills, on_delete=models.CASCADE)
    status = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'staff_skill'








