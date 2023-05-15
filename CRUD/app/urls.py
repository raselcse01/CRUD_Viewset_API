from django.urls import path
from django.urls.conf import include
from app import views

from app.views import StudentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('student', StudentViewSet, basename='student')

urlpatterns = [
    path('', include(router.urls)),
]