from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=64)
    text = models.TextField()
    draft = models.BooleanField(default=True)
    date_published = models.DateTimeField(auto_now=True)
    author = models.ForeignKey("registration.Author",
                               on_delete=models.CASCADE)

    def __str__(self):
        return self.title
