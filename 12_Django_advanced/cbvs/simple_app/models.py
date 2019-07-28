from django.db import models


class School(models.Model):
    name = models.CharField(max_length=256)
    city = models.CharField(max_length=50)
    principal = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    school = models.ForeignKey("simple_app.School",
                               related_name='students',
                               on_delete=models.CASCADE)

    def __str__(self):
        return self.name
