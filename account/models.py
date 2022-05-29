from django.db import models
from utils.choices import Color, Country, Box
from mixins.models import TimestampMixin
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User



class Car(TimestampMixin):
	class Meta:
		verbose_name = "Машина"
		verbose_name_plural = 'Машины'
		ordering = ('year', )
	color = models.CharField(max_length=50, choices=Color.choices, default=Color.WHITE, verbose_name="Цвет")
	company = models.CharField(max_length=50, verbose_name="Компания")
	year = models.IntegerField(verbose_name="Год выпуска")
	country = models.CharField(max_length=50, choices=Country.choices, default=Country.KAZ, verbose_name="Страна выпуска")
	owner = models.CharField(max_length=50, verbose_name="Владелец")
	automatic_box = models.CharField(max_length=50, choices=Box.choices, verbose_name="Вид автомата коробки", null=True)
	insurance_date = models.DateField(verbose_name="Дата страховки", null=True)
	is_damaged = models.BooleanField(default=False, verbose_name="Повреждения")
	name = models.CharField(max_length=50, verbose_name="Название", null=True)
	asd = models.CharField(max_length=50, verbose_name="Что-то", null=True)

	def __str__(self):
		return f'{self.name}'


# class UserSerializer(serializers.ModelSerializer):
#     email = serializers.EmailField(
#             required=True,
#             validators=[UniqueValidator(queryset=User.objects.all())]
#             )
#     username = serializers.CharField(
#             validators=[UniqueValidator(queryset=User.objects.all())]
#             )
#     password = serializers.CharField(min_length=8)
#
#     def create(self, validated_data):
#         user = User.objects.create_user(validated_data['username'], validated_data['email'],
#              validated_data['password'])
#         return user
#
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email', 'password')