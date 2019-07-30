from django.contrib import admin
from registration import models as reg_models
from posts import models as post_models

# Register your models here.
admin.site.register(reg_models.Author)
admin.site.register(post_models.Post)
