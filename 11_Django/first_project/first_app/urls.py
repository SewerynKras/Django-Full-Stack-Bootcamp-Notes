from django.urls import path
from first_app import views


app_name = "first_app"

urlpatterns = [
    path("", views.nested, name='home_page'),
    path("img", views.image),
    path("webpages", views.webpages),
    path("form", views.form, name='register'),
    path("users", views.users, name='users'),
]
