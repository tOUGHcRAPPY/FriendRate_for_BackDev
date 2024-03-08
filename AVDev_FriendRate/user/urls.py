from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .api import UserModelAPIView

router = DefaultRouter()
router.register("", UserModelAPIView)

urlpatterns = [
    path("", include(router.urls)),
]
