from django.db import models
from django.utils.text import slugify
from django.shortcuts import reverse


class Post(models.Model):
    title = models.CharField(max_length=64)
    text = models.TextField()
    draft = models.BooleanField(default=True)
    date_published = models.DateTimeField(auto_now=True)
    author = models.ForeignKey("registration.Author",
                               on_delete=models.CASCADE)
    text_preview = models.TextField(default=" ")
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.text_preview = self.text[:500]
        self.slug = slugify(self.title[:20] + "-" + str(self.author.user.id))
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("posts:drafts")


class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey("registration.Author",
                               on_delete=models.CASCADE)
    post = models.ForeignKey("posts.Post",
                             on_delete=models.CASCADE)
