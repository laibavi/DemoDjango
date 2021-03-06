from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.authentication import views

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
