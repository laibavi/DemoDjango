from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.staff import views

router = DefaultRouter()
# router.register(r'projects', views.ProjectsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
