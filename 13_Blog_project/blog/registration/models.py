from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to="profile_pics",
                                    height_field=None,
                                    width_field=None,
                                    max_length=None,
                                    default='profile_pics/DEFAULT.jpg')
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username
