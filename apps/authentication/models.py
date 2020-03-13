# from .constants import *
from django.db import models
from apps.staff.models import Staffs


class Roles(models.Model):
    role_name = models.CharField(max_length=254)
    status = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'roles'


class User(models.Model):
    role_id = models.ForeignKey(Roles, on_delete=models.CASCADE)
    staff_id = models.ForeignKey(Staffs, on_delete=models.CASCADE)
    email = models.EmailField()
    name = models.CharField(max_length=254)
    password = models.CharField(max_length=254)
    status = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'user'


class PasswordReset(models.Model):
    token = models.CharField(max_length=255)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'password_reset'
