from django.db import models


class Color(models.TextChoices):
    BLACK = ('Bl', 'Black')
    RED = ('R', 'Red')
    WHITE = ('W', 'White')
    BLUE = ('B', "Blue")


class Country(models.TextChoices):
    KAZ = ('K', 'Kaz')
    RUS = ('R', "Rus")
    TUR = ('T', "Tur")
    GER = ('G', "Ger")


class Box(models.TextChoices):
    ROBOT = ('R', 'Robot')
    VARIATOR = ('V', 'Variator')
