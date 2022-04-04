from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from account.models import Car
from account.serializer import CarSerializer


class CarViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    http_method_names = ("get",)
