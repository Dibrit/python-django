from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, CreateModelMixin, UpdateModelMixin
from account.models import Car
from rest_framework.response import Response
from account.serializer import CarSerializer, CarDetailSerializer, CarCreateSerializer, CarChangeColorSerializer
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.response import Response
from .serializer import (
    ChangePasswordSerializer,
    LoginSerializer,
    RegistrationSerializer,
    ForgotPasswordSerializer,
    UserSerializer,
)


class CarViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    http_method_names = ("get", "post")

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CarDetailSerializer
        if self.action == 'create':
            return CarCreateSerializer
        return self.serializer_class

    @action(methods=['post'], detail=True)
    def change_color(self, request, pk):
        instance = self.get_object()
        serializer = CarChangeColorSerializer(instance=instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(CarSerializer(instance=self.get_object()).data)

    @action(methods=['get'], detail=False)
    def white_cars(self, request):
        cars = Car.objects.filter(color="W")
        serializer = CarSerializer(cars, many=True)
        print(serializer.data)
        return Response(serializer.data)


class RegistrationViewSet(CreateModelMixin, GenericViewSet):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer


class LoginViewSet(CreateModelMixin, GenericViewSet):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer


class ChangePasswordViewSet(CreateModelMixin, GenericViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer


class ForgotPasswordViewSet(CreateModelMixin, GenericViewSet):
    permission_classes = (AllowAny,)
    serializer_class = ForgotPasswordSerializer


class UserViewSet(GenericViewSet, ListModelMixin):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.request.user)
        return Response(serializer.data)