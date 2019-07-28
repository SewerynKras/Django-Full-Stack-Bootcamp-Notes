from django.db import models
from django.urls import reverse


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

    def get_absolute_url(self):
        return reverse("simple_app:detail", kwargs={"pk": self.school.pk})
