from rest_framework.routers import DefaultRouter

from .api import UserModelAPIView

router = DefaultRouter()
router.register("", UserModelAPIView)

urlpatterns = router.urls

