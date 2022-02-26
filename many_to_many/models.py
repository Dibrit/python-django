from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=30)
    courses = models.ManyToManyField(Course, related_name='students')

    def __str__(self):
        return self.name
