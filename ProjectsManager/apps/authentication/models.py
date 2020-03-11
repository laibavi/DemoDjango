# from .constants import *
from django.db import models
from apps.staff.models import Staffs


class Roles(models.Model):
    role_name = models.CharField(max_length=254, null=False)
    status = models.IntegerField(default=1, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)


class User(models.Model):
    role_id = models.ForeignKey(Roles, on_delete=models.CASCADE, null=False)
    staff_id = models.ForeignKey(Staffs, on_delete=models.CASCADE, null=False)
    email = models.EmailField(null=False)
    name = models.CharField(max_length=254, null=False)
    password = models.CharField(max_length=254, null=False)
    status = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)


class PasswordReset(models.Model):
    token = models.CharField(max_length=255, null=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)