import rest_framework
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from apps.project import views

router = DefaultRouter()

router.register(r'projects/plans', views.ProjectsPlansViewSet)

urlpatterns = [
    path('', include(router.urls)),
]