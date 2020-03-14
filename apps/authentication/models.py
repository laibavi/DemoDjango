# from .constants import *
from django.db import models
from apps.staff.models import Staffs


class Roles(models.Model):
    role_name = models.CharField(max_length=255)
    status = models.BooleanField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'roles'

    def __str__(self):
        return self.role_name


class Users(models.Model):
    role = models.ForeignKey(Roles, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staffs, on_delete=models.CASCADE)
    email = models.EmailField()
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    status = models.BooleanField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.name


class PasswordResets(models.Model):
    token = models.CharField(max_length=255)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'password_resets'
