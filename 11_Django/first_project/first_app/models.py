from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Topic(models.Model):
    topic_name = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.topic_name


class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.name


class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)


class ExtendedUser(models.Model):
    # instead of creating a new User model you can
    # just extend the built in version
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to="profile_pics",
                                    height_field=None,
                                    width_field=None,
                                    max_length=None,
                                    blank=True)

    def __str__(self):
        return self.user.username
