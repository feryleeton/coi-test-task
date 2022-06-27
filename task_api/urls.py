from django.urls import include, path
from rest_framework import routers
from task_api.views import CategoryViewSet, DoctorViewSet

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'doctors', DoctorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]