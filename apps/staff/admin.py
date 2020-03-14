from django.contrib import admin
from .models import Staffs, Groups, Positions

# Register your models here.

admin.site.register(Staffs)
admin.site.register(Groups)
admin.site.register(Positions)