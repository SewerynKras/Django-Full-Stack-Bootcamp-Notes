from django.urls import path
from posts.views import IndexView


app_name = "posts"

urlpatterns = [
    path("", IndexView.as_view(), name='homepage')
]
