from django.urls import path, include
from django.urls import path, include
from rest_framework import routers
from .views import (
    LoginViewSet,
    RegistrationViewSet,
    ChangePasswordViewSet,
    ForgotPasswordViewSet,
    UserViewSet
)
from rest_framework.routers import DefaultRouter
from .views import CarViewSet


app_name = "account"

router = DefaultRouter()
router.register(r"car", CarViewSet)
router.register(r"register", RegistrationViewSet, basename="register")
router.register(r"login", LoginViewSet, basename="login")
router.register(r"change_password", ChangePasswordViewSet, basename="change_password")
router.register(r"forgot_password", ForgotPasswordViewSet, basename="forgot_password")
router.register(r"", UserViewSet, basename="user")
urlpatterns = [
    path("", include(router.urls)),
]
