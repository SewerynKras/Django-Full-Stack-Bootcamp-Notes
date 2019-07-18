from django.db import models


# Create your models here.
class User(models.Model):
    first_name = models.TextField(max_length=24)
    last_name = models.TextField(max_length=24)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.first_name + " " + self.last_name
