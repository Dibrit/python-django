from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import CarViewSet


app_name = "account"

router = DefaultRouter()
router.register(r"car", CarViewSet, base_name="car")

urlpatterns = router.urls
