from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to="profile_pics",
                                    height_field=100,
                                    width_field=100,
                                    max_length=None,
                                    blank=True)

    def __str__(self):
        return self.user.username
